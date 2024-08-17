/* Скрыть / показать папку */
function toggleDisplay(element) {
    if (element.style.display == "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

function setDisplayBlock(element) {
    if (element.style.display == "none") {
        element.style.display = "block";
    }
}

/* Изменение размера шрифта */
function changeFontSize(element, action) {
    let currentSize = parseFloat(getComputedStyle(element).fontSize);

    if (action === "+") {
        element.style.fontSize = (currentSize + 2) + "px";
        currentSize += 2
    } else if (action === "-") {
        if (currentSize < 3) return
        element.style.fontSize = (currentSize - 2) + "px";
        currentSize -= 2
    } else if (action === "=") {
        element.style.fontSize = 12 + "px";
        currentSize = 12
    }

    let FontSizeElement = document.getElementById("FontSizeSize");

    if (typeof FontSizeElement.innerText != "undefined") {
        FontSizeElement.innerText = currentSize + "px"; // IE8-
    } else {
        FontSizeElement.textContent = currentSize + "px"; // Нормальные браузеры
    }
}

/* Копирование всего текста */
function copyTextFromDiv(element) {
    var text = element.innerText;
    console.log(text);
    var textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    textArea.remove();
}

/*Копировать выделенный текст*/
function copyTextFromDiv2() {
    document.execCommand("copy");
}

/*Изменить цвет кнопки справа*/
function changeColor(element) {
    element.style.backgroundColor = "#008000";
    setTimeout(function() {element.style.backgroundColor = "#525252";}, 2000);
}

/*Вставить шпаргалку*/
function PutHtmlText(html) {
    if (!html) {
        html = '<img alt="404.png" src="404.png">'
    }
    let FieldElement = document.getElementById("field");

    if (typeof FieldElement.innerText != "undefined") {
        FieldElement.innerHTML = html; // IE8-
    } else {
        FieldElement.textContent = html; // Нормальные браузеры
    }
    FieldElement.scrollTo(0, 0);
    processingCheatSheet(FieldElement);
}

/*Взять нужную шпаргалку по пути*/
function getCheatSheat(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, false); // Используется синхронный запрос
    xhr.send();

    if (xhr.status === 200) {
        return xhr.responseText;
    } else {
        return "";
    }
}

function removeSuffix(str, suffix) {
  if (str.endsWith(suffix)) {
    return str.slice(0, -suffix.length);
  }
  return str;
}

function GET(url) {
    url = removeSuffix(url, "index.md");
    addArgumentToUrl(url);
    if (!url.endsWith(".md") && !url.endsWith(".html") && url !== "settings") {
        if (isCtrlPressed) {
            return
        }
        url += "index.md";
    }

    if (need_save_history) {
        if (!(url in history)) {
            cs = getCheatSheat(url);
            if (cs) {
                history[url] = cs
            }
            console.log(`GET "${url}"`)
        } else {
            console.log(`GET history["${url}"]`)
        }
        cheatsheet = history[url];
        if (cheatsheet === undefined) {cheatsheet = "";}
    } else {
        cheatsheet = getCheatSheat(url);
        console.log(`GET "${url}"`)
    }
    PutHtmlText(cheatsheet);
}

function copyCode(button_element) {
    let code_element = button_element.parentElement.parentElement.lastElementChild;

    const pre_element = document.createElement("pre");
    pre_element.innerHTML = code_element.innerHTML;
    if (!isCtrlPressed) {
        const elementsToRemove = pre_element.querySelectorAll(".unselectable");
        elementsToRemove.forEach(element => element.remove());
    }
    const textarea = document.createElement("textarea");
    document.body.appendChild(textarea);
    textarea.value = pre_element.textContent;
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);

    let svg = '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">'
    let html1 = svg + '<polyline points="20 6 9 17 4 12"></polyline></svg><text>Copied!</text>';
    let html2 = svg + '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text>';

    if (typeof button_element.innerText != "undefined") {
         button_element.innerHTML = html1; // IE8
    } else {
         button_element.textContent = html1; // Нормальные браузеры
    }

    setTimeout(function() {
        if (typeof button_element.innerText != "undefined") {
             button_element.innerHTML = html2; // IE8
        } else {
             button_element.textContent = html2; // Нормальные браузеры
        }
    }, 1000);
}

function downloadTextFile(text, filename) {
  // Создаем элемент <a> для загрузки файла
  const element = document.createElement("a");
  element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
  element.setAttribute("download", filename);

  // Скрытый элемент <a>, добавляем его в DOM
  element.style.display = "none";
  document.body.appendChild(element);

  // Симулируем щелчок по элементу для загрузки файла
  element.click();

  // Удаляем элемент из DOM
  document.body.removeChild(element);
}

function DownloadCode(button_element, filename) {
    let code_element = button_element.parentElement.parentElement.lastElementChild;

    let text = code_element.textContent
    downloadTextFile(text.split("\n").slice(1).join("\n"), filename);

    let download_html = '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 3v4a1 1 0 0 1-1 1H5m5 4-2 2 2 2m4-4 2 2-2 2m5-12v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z"/></svg><pre>Download code</pre>'
    let downloaded_html = '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><polyline points="20 6 9 17 4 12"></polyline></svg><pre>Download!</pre>';

    if (typeof button_element.innerText != "undefined") {
         button_element.innerHTML = downloaded_html; // IE8
    } else {
         button_element.textContent = downloaded_html; // Нормальные браузеры
    }

    setTimeout(function() {
        if (typeof button_element.innerText != "undefined") {
             button_element.innerHTML = download_html; // IE8
        } else {
             button_element.textContent = download_html; // Нормальные браузеры
        }
    }, 1000);
}

function addArgumentToUrl(arg) {
    const currentUrl = new URL(window.location.href);
    currentUrl.search = arg;
    window.history.pushState({}, "", currentUrl);
}

function getArgumentFromUrl() {
    const currentUrl = new URL(window.location.href);
    return currentUrl.search ? currentUrl.search.substring(1) : null;
}

function removeArgumentFromUrl() {
    let url = new URL(window.location.href);
    url.search = "";
    window.history.replaceState(null, null, url.href);
}

function addSearchArgumentToUrl(arg) {
    const currentUrl = new URL(window.location.href);
    currentUrl.search = arg;
    window.history.pushState({}, "", currentUrl);
}

function getPathWithoutFilename(filePath) {
    filePath = decodeURIComponent(filePath);
    if (filePath.endsWith("/")) {
        return filePath
    }
    const lastSlashIndex = filePath.lastIndexOf("/");
    if (lastSlashIndex !== -1) {
        return filePath.substring(0, lastSlashIndex);
    }
   return "";
}

function toggleStyleDisplayByPath(kpath) {
    let element = document.querySelector(`[kpath="${kpath}"]`);
    element.click();
    let parent = element.parentElement;
    while (parent) {
        setDisplayBlock(parent);
        parent = parent.parentElement;
    }
}

function restoreCheatSheetState(path) {
    let kpath = getPathWithoutFilename(path);
    let kelement = document.querySelector(`[kpath="${kpath}"]`);
    if (!kelement) {
        kpath += "/";
        kelement = document.querySelector(`[kpath="${kpath}"]`);
    }
    // console.log("getPathWithoutFilename", kpath);
    try {
        toggleStyleDisplayByPath(kpath);
    } catch (e) {
        console.log(`toggleStyleDisplayByPath("${kpath}");`);
    }

    let vpath = path;
    let velement = document.querySelector(`[vpath="${vpath}"]`);
    if (!velement) {
        vpath += "/";
        velement = document.querySelector(`[vpath="${vpath}"]`);
    }
    if (!velement) {
        return PutHtmlText();
    }
    // console.log("vpath", vpath);

    const container = document.querySelector(".cheatsheet-buttons");
    if (vpath.endsWith("/")) {
        velement.click();
    }
    velement.focus();
    if (vpath.endsWith("/")) {
        console.log(`click "${vpath}"`)
        velement.click();
    }
    velement.scrollIntoView({block: "center"});
    container.scrollLeft -= 200;
    GET(path);
}

function performSearch(search_query) {
    if (!search_query) {return}
    console.log("Search:", search_query);
    const searchButtonFolder = document.getElementById("search-button-folder");
    const cheatsheetButtons = document.getElementById("cheatsheet-buttons");

    if (search_query) {
        searchButtonFolder.style.display = "block";
    } else {
        searchButtonFolder.style.display = "none"
    }
    searchButtonFolder.innerHTML = "";
    s1Array = [];
    let searchElement = document.getElementById("search");

    if (settings["settings-search-regex"]) {
        for (el of search_query.split(" ").filter(item => item !== "")) {
            try {
                s1Array.push(new RegExp(el, settings["settings-search-register-independence"] ? "i" : ""));
                searchElement.style.color = "#AFB1B3";
            } catch (e) {
                searchElement.style.color = "#ff0000";
            }
        }
    } else {
        searchElement.style.color = "#AFB1B3";
        if (settings["settings-search-register-independence"]) {
            search_query = search_query.toLowerCase()
        };
        s1Array = search_query.split(" ").filter(item => item !== "")
    }
    console.log(s1Array);

    function searchElements(element) {
        let results = [];
        for (el of element)
            if (el.tagName === "BUTTON" && el.getAttribute("vpath")) {
                vpath = el.getAttribute("vpath");
                if (settings["settings-search-register-independence"]) {
                    vpath = vpath.toLowerCase();
                }
                let s2Array = vpath.replace(".md", "").split("/");
                if (!settings["settings-search-full-path"]) {
                    slc1 =  s2Array.slice(-1)
                    if (slc1[0] === "index") {
                        s2Array = s2Array.slice(-2, -1);
                    } else {
                        s2Array = s2Array.slice(-1);
                    }
                };
                if (s1Array.every(ss1 => s2Array.some(ss2 =>
                    settings["settings-search-regex"] ? ss2.match(ss1) : ss2.includes(ss1 ? ss1 : null)
                ))) {
                    results.push(el);
                }
            } else {
                results = results.concat(searchElements(el.children));
            }
        return results;
    };
    results = searchElements(Array.from(cheatsheetButtons.children).slice(2));
    console.log("found", results.length, "results")
    if (results.length > 0) {
        console.log(results.map(item => item.getAttribute("vpath")));
        results.forEach(element => {
            vpath = element.getAttribute("vpath");
            title = removeSuffix(removeSuffix(vpath, ".md"), "/⁠index");

            button = document.createElement("button");
            if (settings["settings-search-show-full-path"]) {
                button.innerHTML = element.firstElementChild.outerHTML + title;
            } else {
                button.innerHTML = element.innerHTML;
            }
            button.classList.add("button");
            button.setAttribute("vpath", vpath);
            button.setAttribute("onclick", "GET(this.getAttribute(`vpath`));restoreCheatSheetState(this.getAttribute(`vpath`));delAnchor();");
            button.setAttribute("title", title);
            searchButtonFolder.appendChild(button);
        });
    } else {
        button = document.createElement("button");
        button.textContent = "Nothing found";
        button.classList.add("button");
        button.setAttribute("title", "Nothing found");
        searchButtonFolder.appendChild(button);
    }
}

function saveSettings(settings) {
    localStorage.setItem("settings", JSON.stringify(settings));
}

function loadSettings() {
    const settings = localStorage.getItem("settings");
    return settings ? JSON.parse(settings) : {
        "settings-search-regex": false,
        "settings-search-register-independence": true,
        "settings-search-full-path": true,
        "settings-search-show-full-path": true,
    };
}


document.addEventListener("DOMContentLoaded", function() {
    // Аргументы URL
    const arg = decodeURIComponent(getArgumentFromUrl());
    if (arg !== "null") {
        console.log(`Argument found: "${arg}"`);
        restoreCheatSheetState(arg);
    } else {
        PutHtmlText(getCheatSheat("README.html"));
    }

    // Якорь
    const anchor = getAnchor();
    if (anchor) {
        console.log(`Anchor found: "${anchor}"`);
        anchor_element = document.getElementById(anchor)
        if (anchor_element) anchor_element.scrollIntoView({block: "start"});
    }

    // Поиск
    const searchInput = document.getElementById("search");
    searchInput.addEventListener("input", function() {
        performSearch(searchInput.value);
    });

    // Изменялка размеров #cheatsheet-buttons и #field
    const rpanrResize = document.getElementById("rpanrResize");
    rpanrResize.addEventListener("mousedown", mD);
    rpanrResize.addEventListener("touchstart", mD);

    // Настройки
    const settingsOverlay = document.getElementById("settings-overlay");
    const settingsPopup = document.getElementById("settings-popup");
    const settingsButton = document.getElementById("settings-button");
    const settingsOkButton = document.getElementById("settings-ok-button");
    const settingsResetButton = document.getElementById("settings-reset-button");

    settingsButton.addEventListener("click", () => {settingsOverlay.style.display = "block";settingsPopup.style.display = "block";});
    settingsOverlay.addEventListener("click", () => {settingsOverlay.style.display = "none";settingsPopup.style.display = "none";});
    settingsOkButton.addEventListener("click", () => {settingsOverlay.style.display = "none";settingsPopup.style.display = "none";});
    settingsResetButton.addEventListener("click", () => {
        settings["settings-search-regex"] = false;
        settings["settings-search-register-independence"] = true;
        settings["settings-search-full-path"] = true;
        settings["settings-search-show-full-path"] = true;
        saveSettings(settings);
        applySettings(settings);
        performSearch(searchInput.value);
    });

    applySettings(settings);
    document.getElementById("settings-popup").childNodes.forEach((element) => {
        if (element.tagName === "INPUT") {
            element.addEventListener("change", (event) => {
                settings[element.id] = event.target.checked;
                console.log(`settings["${element.id}"] = "${event.target.checked}"`);
                saveSettings(settings);
                performSearch(searchInput.value);
            });
        }
    });
});
document.addEventListener("keydown", function(event) {if (event.ctrlKey) {isCtrlPressed = true;}});
document.addEventListener("keyup", function(event) {if (!event.ctrlKey) {isCtrlPressed = false;}});
document.addEventListener("click", function(event) {
    if (event.target.tagName === "CODE") {
        const tempInput = document.createElement("input");
        document.body.appendChild(tempInput);
        tempInput.value = event.target.textContent;
        tempInput.select();
        document.execCommand("copy");
        document.body.removeChild(tempInput);
    }
});


let need_save_history = true;
let history = {};
let isCtrlPressed = false;
let ismdwn = 0;
let settings = loadSettings();


function mD(event) {
    event.preventDefault(); // Предотвращаем стандартное поведение браузера
    ismdwn = 1;
    document.body.addEventListener("mousemove", mV);
    document.body.addEventListener("mouseup", end);
    document.body.addEventListener("touchmove", mV);
    document.body.addEventListener("touchend", end);
}

function mV(event) {
    let clientX;
    if (event.type === "mousemove" || event.type === "mouseup") {
        clientX = event.clientX;
    } else if (event.type === "touchmove") {
        clientX = event.touches[0].clientX;
    }

    if (ismdwn === 1) {
        const cheatsheetButtons = document.getElementById("cheatsheet-buttons");
        cheatsheetButtons.style.flexBasis = clientX - 48 + "px";
    } else {
        end();
    }
}

function end() {
    ismdwn = 0;
    document.body.removeEventListener("mousemove", mV);
    document.body.removeEventListener("mouseup", end);
    document.body.removeEventListener("touchmove", mV);
    document.body.removeEventListener("touchend", end);
}

function setAnchor(anchor) {
    const url = new URL(window.location.href);
    url.hash = anchor ? `#${anchor}` : "";
    window.history.pushState({}, "", url.toString());
};

function delAnchor() {
    const url = new URL(window.location.href);
    url.hash = "";
    window.history.pushState({}, "", url.toString());
};

function getAnchor() {
    const url = new URL(window.location.href);
    return url.hash ? url.hash.slice(1) : null;
};

function processingCheatSheet(element) {
    element.querySelectorAll("a").forEach(a => {
        if (!a.target) {a.target="_blank";}
    });
    element.querySelectorAll("h1, h2, h3, h4, h5, h6").forEach(header => {
        let id = header.textContent.trim()
            .toLowerCase()
            .replace(/\s+/g, "-")
            // .replace(/[^\w\-]+/g, "")
            .replace(/\-\-+/g, "-")
            .replace(/^-+/, "")
            .replace(/-+$/, "");
        header.id = id;
        header.innerHTML = `${header.innerHTML}<a class="anchor" href="#${id}"><svg style="width: .6em;height: .9em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.213 9.787a3.391 3.391 0 0 0-4.795 0l-3.425 3.426a3.39 3.39 0 0 0 4.795 4.794l.321-.304m-.321-4.49a3.39 3.39 0 0 0 4.795 0l3.424-3.426a3.39 3.39 0 0 0-4.794-4.795l-1.028.961"></path></svg></a>`;
    });
};

function applySettings(settings) {
    for (const [key, value] of Object.entries(settings)) {
        const element = document.getElementById(key);
        if (element) element.checked = value;
    }
};
