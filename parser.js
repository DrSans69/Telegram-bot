// const link = process.argv[2];
const link =
    "https://www.olx.ua/d/uk/obyavlenie/novyy-detskiy-podrostkovyy-kvadrotsikl-comman-rival-125cc-motosalon-IDT8NXF.html";

const puppeteer = require("puppeteer");

const scrapeData = async (url) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto(url, { waitUntil: "domcontentloaded" });

    const slideWrapper = await page.evaluate(() => {
        const swiperWrapperElement = document.querySelector(".swiper-wrapper");
        return swiperWrapperElement ? swiperWrapperElement.innerHTML : null;
    });

    await browser.close();

    return slideWrapper;
};

if (!link) {
    console.error("Please provide a valid link as a command-line argument.");
    process.exit(1);
}

scrapeData(link)
    .then((result) => {
        if (result) {
            console.log("Contaier\n:", result);
        } else {
            console.log("Could not find .swiper-wrapper element on the page.");
        }
    })
    .catch((error) => {
        console.error("Error:", error);
    });
