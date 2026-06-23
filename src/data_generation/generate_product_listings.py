from src.database.connection import get_connection

STORE_MAPPING = {
    "Sony": ["Amazon", "Flipkart", "Croma", "Reliance Digital", "Vijay Sales"],   # Sony
    "Apple": ["Amazon", "Flipkart", "Apple Store"],                                # Apple
    "Samsung": ["Amazon", "Flipkart", "Croma", "Reliance Digital"],                  # Samsung
    "OnePlus": ["Amazon", "Flipkart"],                                               # OnePlus
    "Bose": ["Amazon", "Flipkart"],                                               # Bose
    "JBL": ["Amazon", "Flipkart"],                                               # JBL
    "Sennheiser": ["Amazon", "Flipkart"],                                               # Sennheiser
    "Google": ["Amazon", "Flipkart"],                                               # Google
    "Dell": ["Amazon", "Reliance Digital"],                                       # Dell
    "HP": ["Amazon", "Reliance Digital"],                                      # HP
    "Lenovo": ["Amazon", "Reliance Digital"],                                      # Lenovo
    "Asus": ["Amazon", "Reliance Digital"]                                       # Asus
}


PRODUCT_URL_MAPPING = {
    ("Sony WH-1000XM5", "Amazon"):
        "https://www.amazon.in/Sony-WH-1000XM5-Wireless-Cancelling-Headphones/dp/B09XS7JWHH?th=1",
    
    ("Sony WH-1000XM5", "Flipkart"):
        "https://www.flipkart.com/sony-wh1000xm5-silver-bluetooth-wired/p/itm96f759ebab85d",

    ("Sony WH-1000XM5", "Croma"):
        "https://www.croma.com/sony-wh-1000xm5-bluetooth-headphone-with-mic-auto-noise-cancellation-optimizer-over-ear-black-/p/262565?srsltid=AfmBOopPTJxiWicuY4fzsOPWEcRyqrjkx2LnrRLMOmQcyewR2sJj4rUu",
    
    ("Sony WH-1000XM5", "Reliance Digital"):
        "https://www.reliancedigital.in/product/sony-wh-1000xm5-bluetooth-headphone-with-30-hours-battery-life-black-l88xiz",
    
    ("Sony WH-1000XM5", "Vijay Sales"):
        "https://www.vijaysales.com/p/P206834/206834/sony-wh-1000xm5-wireless-industry-leading-noise-canceling-headphones-with-auto-noise-canceling-up-to-30-hours-battery-life-black",
    
    ("Bose QuietComfort Ultra", "Amazon"):
        "https://www.amazon.in/Bose-QuietComfort-Bluetooth-Headphones-Cancelling/dp/B0FDKR293G?th=1",
    
    ("Bose QuietComfort Ultra", "Flipkart"):
        "https://www.flipkart.com/bose-quietcomfort-ultra-bluetooth-headphones-2nd-gen-wired/p/itmb6a7f56e22dde",

    ("JBL Live 770NC", "Amazon"):
        "https://www.amazon.in/JBL-Cancellation-Headphones-Multipoint-Personi-Fi/dp/B0CHMN4KVN?th=1",

    ("JBL Live 770NC", "Flipkart"):
        "https://www.flipkart.com/jbl-live-770nc-anc-65hr-playtime-speed-charge-bt-5-3-le-audio-personify-2-0-bluetooth-headset/p/itm325a6e705b889",

    ("Sennheiser Momentum 4", "Amazon"):
        "amazon.in/Sennheiser-Momentum-Wireless-Headphones-Crystal-Clear/dp/B0B6GHW1SX",
    
    ("Sennheiser Momentum 4", "Flipkart"):
        "https://www.flipkart.com/sennheiser-momentum-4-wireless-anc-60-hours-battery-life-bluetooth-headset/p/itm8c609112faa10",
    
    ("OnePlus Nord Wired Headphones", "Amazon"):
        "https://www.amazon.in/OnePlus-Nord-Wired-Earphones-3-5Mm/dp/B0D9NG5Q6R",
    
    ("OnePlus Nord Wired Headphones", "Flipkart"):
        "https://www.flipkart.com/oneplus-nord-wired-earphones/p/itmeda77ab3975bd",
    
    ("Sony WH-CH720N", "Amazon"):
        "https://www.amazon.in/Sony-Cancellation-Headphones-Multi-Point-Connection/dp/B0BS1QCFHX?th=1",
    
    ("Sony WH-CH720N", "Flipkart"):
        "https://www.flipkart.com/sony-wh-ch720n-active-noise-cancelling-50-hrs-battery-life-multipoint-connection-bluetooth-headset/p/itm2372dae5e7e59",
    
    ("Sony WH-CH720N", "Croma"):
        "https://www.croma.com/sony-wh-ch720n-bluetooth-headphone-with-mic-dual-noise-sensor-technology-over-ear-black-/p/270320?srsltid=AfmBOoqgKxCkkpTlaRpbNgLzHJ-lZmxUSg5S5NkFbEwXR2htX4JoiZEf",
    
    ("Sony WH-CH720N", "Reliance Digital"):
        "https://www.reliancedigital.in/product/sony-wh-ch720n-over-the-ear-bluetooth-headphone-with-active-noise-cancellation-blue-lglsog",
    
    ("Sony WH-CH720N", "Vijay Sales"):
        "https://www.vijaysales.com/p/P216071/216072/sony-wh-ch720n-wireless-headphones-with-active-noise-cancellation-with-mic-up-to-35-hours-playtime-blue",

    ("Sony WF-1000XM5", "Amazon"):
        "https://www.amazon.in/Sony-WF-1000XM5-Cancelling-Headphones-Multi-Point/dp/B0C33XXS56?th=1",
    
    ("Sony WF-1000XM5", "Flipkart"):
        "https://www.flipkart.com/sony-wf-1000xm5-best-noise-cancelling-tws-earbuds-multi-point-upto-36hrs-battery-bluetooth-headset/p/itm86886b74b3256",
    
    ("Sony WF-1000XM5", "Croma"):
        "https://www.croma.com/sony-wf-1000xm5-tws-earbuds-with-active-noise-cancellation-ipx4-water-resistant-quick-charge-black-/p/301580?srsltid=AfmBOopQgvHG0ekjVz6vikPg4oZamMw41E3EgKQo895TwLAR0VVdCjBK",
    
    ("Sony WF-1000XM5", "Reliance Digital"):
        "https://www.reliancedigital.in/product/sony-wf1000xm5-tws-earbuds-with-up-to-36-hours-battery-life-and-quick-charge-active-noise-cancellation-sliver-ln0fd4-7534141",
    
    ("Sony WF-1000XM5", "Vijay Sales"):
        "https://www.vijaysales.com/p/221497/sony-wf-1000xm5-truly-wireless-earbuds-with-hd-noise-cancellation-3-minute-quick-charge-24-hours-battery-life-high-res-audio-silver",
    
    ("Apple AirPods Pro (2nd Gen)", "Amazon"):
        "https://www.amazon.in/Apple-AirPods-Generation-MagSafe-USB%E2%80%91C/dp/B0CHX719JD",
    
    ("Apple AirPods Pro (2nd Gen)", "Flipkart"):
        "https://www.flipkart.com/apple-airpods-pro-2nd-generation-magsafe-case-usb-c-bluetooth-headset/p/itm60c8f5a308352",
    
    ("OnePlus Buds Pro 3", "Amazon"):
        "https://www.amazon.in/OnePlus-Buds-Pro-Bluetooth-Ear/dp/B0DBHX75C4",
    
    ("OnePlus Buds Pro 3", "Flipkart"):
        "https://www.flipkart.com/oneplus-buds-pro-3-midnight-opus-bluetooth/p/itmb3b8258254e33",
    
    ("JBL Live Beam 3", "Amazon"):
        "https://www.amazon.in/JBL-Multipoint-Connection-Headphones-Personi-Fi/dp/B0D44H2RG3?th=1",
    
    ("JBL Live Beam 3", "Flipkart"):
        "https://www.flipkart.com/jbl-live-beam-3-hi-res-ldac-audio-anc-tws-smartcase-48h-runtime-wireless-charging-bluetooth-headset/p/itm092a3878f8cc2",
    
    ("Sennheiser Momentum True Wireless 4", "Amazon"):
        "https://www.amazon.in/Sennheiser-TrueResponse-Anti%E2%80%91Wind-Transparency-Black-Copper/dp/B0CTHY2PQ9?th=1",
    
    ("Sennheiser Momentum True Wireless 4", "Flipkart"):
        "https://www.flipkart.com/sennheiser-momentum-true-wireless-4-bt-5-4-30hr-battery-adaptive-anc-bluetooth-headset/p/itmd6a44f35a4c88",
    
    ("Samsung Galaxy Buds3 Pro", "Amazon"):
        "https://www.amazon.in/Samsung-Adaptive-Real-Time-Interpreter-Battery/dp/B0D7M4G3NP",
    
    ("Samsung Galaxy Buds3 Pro", "Flipkart"):
        "https://www.flipkart.com/samsung-galaxy-buds-3-pro-bluetooth/p/itm13f27472805c8",
    
    ("Samsung Galaxy Buds3 Pro", "Croma"):
        "https://www.croma.com/samsung-galaxy-buds3-pro-tws-earbuds-with-active-noise-cancellation-ip57-water-resistant-360-audio-white-/p/311869?srsltid=AfmBOoom49272QJ2AW0EXVuArs8DDZnIjsMZhI5P4D9xs8qZa-5WNowv",
    
    ("Samsung Galaxy Buds3 Pro", "Reliance Digital"):
        "https://www.reliancedigital.in/product/samsung-galaxy-buds-3-pro-true-wireless-buds-gray-lyre9m-7960698",
    
    ("Apple iPhone 16", "Amazon"):
        "https://www.amazon.in/iPhone-16-128-GB-Control/dp/B0DGJHBX5Y",
    
    ("Apple iPhone 16", "Flipkart"):
        "https://www.flipkart.com/apple-iphone-16-white-128-gb/p/itm7c0281cd247be",
    
    ("Apple iPhone 16", "Apple Store"):
        "https://www.apple.com/in/shop/buy-iphone/iphone-16",
    
    ("Apple iPhone 16 Pro", "Amazon"):
        "https://www.amazon.in/iPhone-16-Pro-128-GB/dp/B0DGJ3THPR",
    
    ("Apple iPhone 16 Pro", "Flipkart"):
        "https://www.flipkart.com/apple-iphone-16-pro-white-titanium-128-gb/p/itm50f720fdcec51",
    
    ("Samsung Galaxy S25", "Amazon"):
        "https://www.amazon.in/Samsung-Smartphone-Storage-Snapdragon-ProVisual/dp/B0DSKNLFBG",
    
    ("Samsung Galaxy S25", "Flipkart"):
        "https://www.flipkart.com/samsung-galaxy-s25-5g-navy-128-gb/p/itma8f7f68417976",
    
    ("Samsung Galaxy S25", "Croma"):
        "https://www.croma.com/samsung-galaxy-s25-5g-12gb-ram-128gb-navy-/p/315064",
    
    ("Samsung Galaxy S25", "Croma"):
        "https://www.reliancedigital.in/product/samsung-galaxy-s25-5g-128-gb-12-gb-ram-icyblue-mobile-phone-m6rltr-8878214?search_term=galaxy%20s25&internal_source=search_prompt",
    
    ("Samsung Galaxy S25 Ultra", "Amazon"):
        "https://www.amazon.in/Samsung-Smartphone-Silverblue-Snapdragon-ProVisual/dp/B0DSKNKCYX",
    
    ("Samsung Galaxy S25 Ultra", "Flipkart"):
        "https://www.flipkart.com/samsung-galaxy-s25-ultra-5g-titanium-silverblue-1024-gb/p/itm7d0e1ef71672e",
    
    ("Samsung Galaxy S25 Ultra", "Croma"):
        "https://www.croma.com/samsung-galaxy-s25-ultra-5g-12gb-ram-256gb-titanium-gray-/p/313337?srsltid=AfmBOooEdcISeTzdp6wLul1K0z-SYgWKqoXQ14fn7sdwgvyI1Je24cDx",
    
    ("Samsung Galaxy S25 Ultra", "Reliance Digital"):
        "https://www.reliancedigital.in/product/samsung-galaxy-s25-ultra-5g-256-gb-12-gb-ram-titanium-jetblack-mobile-phone-m6rk1b-8878154",
    
    ("OnePlus 13", "Amazon"):
        "https://www.amazon.in/OnePlus-13-256GB-Midnight-Ocean/dp/B0DPS7FB4J?th=1",
    
    ("OnePlus 13", "Flipkart"):
        "https://www.flipkart.com/oneplus-13-black-eclipse-256-gb/p/itmb4659fd2a037f",
    
    ("Google Pixel 9", "Amazon"):
        "https://www.amazon.in/Google-Pixel-Porcelain-256-RAM/dp/B0DZXZTPN8",
    
    ("Google Pixel 9", "Flipkart"):
        "https://www.flipkart.com/google-pixel-9-porcelain-256-gb/p/itm5364256d5efe2",
    
    ("Google Pixel 9 Pro", "Amazon"):
        "https://www.amazon.in/Google-Pixel-Pro-Obsidian-Storage/dp/B0FLQQF6YP",
    
    ("Google Pixel 9 Pro", "Flipkart"):
        "https://www.flipkart.com/google-pixel-9-pro-obsidian-256-gb/p/itm20409981866f4",
    
    ("Samsung Galaxy A56", "Amazon"):
        "https://www.amazon.in/Samsung-Galaxy-Awesome-Gemini-Intelligence/dp/B0DYDPBM8K?th=1",
    
    ("Samsung Galaxy A56", "Flipkart"):
        "https://www.flipkart.com/samsung-galaxy-a56-5g-awesome-graphite-256-gb/p/itm33a726cc39ea5",
    
    ("Samsung Galaxy A56", "Croma"):
        "https://www.croma.com/samsung-galaxy-a56-5g-8gb-ram-256gb-awesome-graphite-/p/314434?srsltid=AfmBOorHJ3KbkovizzkOqW95Z73LW_yY59YvF2ubCsYxSG2FmZPcop5j",
    
    ("Samsung Galaxy A56", "Reliance Digital"):
        "https://www.reliancedigital.in/product/samsung-galaxy-a56-5g-256-gb-8-gb-ram-awesome-graphite-mobile-phone-m7x9g6-8968989",
    
    ("Apple Watch Series 10", "Amazon"):
        "amazon.in/Apple-Cellular-Smartwatch-Titanium-Resistant/dp/B0DGJ3Y24B/ref=sr_1_7?dib=eyJ2IjoiMSJ9.EoCnDMQnFM0nTLhVq-Y_Z1CGovAvOtux8o9G_tZvvYNNG01pYebNmfc13WqsVa3gag6gTMRNliDZzHc_cZbC0RRPijt2vNCnCl6UTOx3wYwoosE-QLnnTA4eR2E6yRX_rkXP_w_oMvqwhn1NsdV_CfYsU3t5EEfkN4I5EQ2E1edk5PsUbUZD-OtEOTxzqLJ5k7753O1AAJqzNR0zdloXuizjuysUyyqU0ahZnadL4u4.JGjM3CEv-O6S8yFW5fiaXeUpVqo_80_sEfC3JB1mf4Q&dib_tag=se&keywords=apple+watch+series+10&nsdOptOutParam=true&qid=1782037003&sr=8-7",
    
    ("Apple Watch Series 10", "Flipkart"):
        "https://www.flipkart.com/apple-watch-series-10-gps-42mm-jet-black-aluminium-ink-sport-loop/p/itmcc9edfed08414",
    
    ("Samsung Galaxy Watch Ultra", "Amazon"):
        "https://www.amazon.in/Samsung-Battery-Processor-Sapphire-Titanium/dp/B0D7M54GMJ?th=1",
    
    ("Samsung Galaxy Watch Ultra", "Flipkart"):
        "https://www.flipkart.com/samsung-galaxy-watch-ultra-2025/p/itm98f919ae6332f",
    
    ("Samsung Galaxy Watch Ultra", "Croma"):
        "https://www.croma.com/samsung-galaxy-watch-ultra-wi-fi+4g-sim-wear-os-smartwatch-37-3mm-super-amoled-display-3nm-processor-dual-frequency-gps-dark-gray-strap-/p/308296?srsltid=AfmBOortvTWayqeQukySoM2j_ymP0eL5ha9rfhwdQ2ZHy-bEIKadB8h2",
    
    ("Samsung Galaxy Watch Ultra", "Reliance Digital"):
        "https://www.reliancedigital.in/product/samsung-watch-ultra-smart-watch-titanium-gray-sm-l705fdaains-lyofey-7918096",
    
    ("Samsung Galaxy Watch 7", "Amazon"):
        "https://www.amazon.in/Samsung-44mm-Green-BT-LTE/dp/B0DKFT7RCN",
    
    ("Samsung Galaxy Watch 7", "Flipkart"):
        "https://www.flipkart.com/samsung-galaxy-watch7-44mm-lte/p/itmf8bef51645876",
    
    ("Samsung Galaxy Watch 7", "Croma"):
        "https://www.croma.com/samsung-galaxy-watch7-wi-fi+4g-sim-wear-os-smartwatch-37-3mm-super-amoled-display-3nm-processor-dual-frequency-gps-silver-strap-/p/308294?srsltid=AfmBOooOO5U2INqVUbHuGPpQM4XN48vm-Xyt0Jq6TTbL9yyco-1Yvrti",
    
    ("Samsung Galaxy Watch 7", "Reliance Digital"):
        "https://www.reliancedigital.in/product/samsung-galaxy-watch-7-40-mm-bluetooth-smart-watch-cream-sm-l300nzeains-lyofez-7918098",
    
    ("OnePlus Watch 2", "Amazon"):
        "https://www.amazon.in/OnePlus-Snapdragon-Stainless-Frequency-Bluetooth/dp/B0CVQDZWVX?th=1",
    
    ("OnePlus Watch 2", "Flipkart"):
        "https://www.flipkart.com/oneplus-watch-2-wear-os-4-snapdragon-w5-chipset-up-100-hours-battery-smartwatch/p/itm417a52b0b57f8",    

    ("Apple Watch SE", "Amazon"):
        "https://www.amazon.in/Apple-Watch-GPS-44mm-Aluminium/dp/B09G9RWJMK",
    
    ("Apple Watch SE", "Flipkart"):
        "https://www.flipkart.com/apple-watch-se-3-2025-gps-44mm-midnight-aluminium-case-sport-band-s-m/p/itm09ae49954778a",
    
    ("Apple Watch SE", "Apple Store"):
        "https://www.apple.com/in/shop/buy-watch/apple-watch-se/40mm-gps-midnight-aluminium-midnight-sport-band-sm-se",
    
    ("Google Pixel Watch 3", "Amazon"):
        "https://www.amazon.in/Google-Pixel-Watch-Latest-Model/dp/B0D91268TH?th=1",
    
    ("Google Pixel Watch 3", "Flipkart"):
        "https://www.flipkart.com/google-pixel-watch-3-45-mm-display-advanced-motion-sensing-smartwatch/p/itma9b91d1b9d39d",
    
    ("Apple MacBook Air M4", "Amazon"):
        "https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDV7GC?th=1",
    
    ("Apple MacBook Air M4", "Flipkart"):
        "https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mw123hn-a/p/itm08069ed2395aa",
    
    ("Apple MacBook Air M4", "Apple Store"):
        "https://www.apple.com/in/shop/buy-mac/macbook-air",
    
    ("Apple MacBook Pro M4", "Amazon"):
        "https://www.amazon.in/Apple-2024-MacBook-Laptop-10%E2%80%91core/dp/B0DLHXVCXJ",
    
    ("Apple MacBook Pro M4", "Flipkart"):
        "https://www.flipkart.com/apple-m4-16-gb-512-gb-ssd-macos-sequoia-mw2w3hn-a/p/itm4a2cfa5fedc01",
    
    ("Apple MacBook Pro M4", "Apple Store"):
        "https://www.apple.com/in/shop/buy-mac/macbook-pro",
    
    ("Dell XPS 13", "Amazon"):
        "https://www.amazon.in/Dell-Snapdragon-Dual-Core-LPDDR5X-Graphite/dp/B0DPM7XJYM/ref=ast_sto_dp_puis",

    ("Dell XPS 13", "Reliance Digital"):
        "https://www.reliancedigital.in/product/dell-new-xps-13-xps-9345-notebook-laptop-qualcomm-snapdragon-x1e-80-10032-gb1-tb-ssdwindows-11ms-officeoledtouchscreen-3302-cm-13-inch-graphite-lyzrpx-8052136?internal_source=search_results",
    
    ("HP Spectre x360", "Amazon"):
        "https://www.amazon.in/HP-Spectre-Enhanced-16-inch-aa0665TU/dp/B0CRKP9ZML/ref=pd_lpo_d_sccl_1/257-2562931-3618311?pd_rd_w=sLZta&content-id=amzn1.sym.e0c8139c-1aa1-443c-af8a-145a0481f27c&pf_rd_p=e0c8139c-1aa1-443c-af8a-145a0481f27c&pf_rd_r=RDYAF6RRHDQMV3G42BRF&pd_rd_wg=3oaIQ&pd_rd_r=37295623-5221-4170-a4c4-a97b506d054c&pd_rd_i=B0CRKP9ZML&psc=1",
    
    ("HP Spectre x360", "Reliance Digital"):
        "https://reliancedigital.in/hp-spectre-x360",
    
    ("Lenovo Yoga 9i", "Amazon"):
        "https://www.amazon.in/Lenovo-Powered-Touchscreen-LPDDR5X-Thunderbolt/dp/B0DBZWY9FZ",
    
    ("Lenovo Yoga 9i", "Reliance Digital"):
        "https://reliancedigital.in/lenovo-yoga-9i",
    
    ("Asus Zenbook 14 OLED", "Amazon"):
        "https://www.amazon.in/ASUS-Zenbook-screen-Windows-UX3405CA-PZ162WS/dp/B0DSHTHR67?th=1",
    
    ("Asus Zenbook 14 OLED", "Reliance Digital"):
        "https://www.reliancedigital.in/product/asus-zenbook-14-ux3405ca-pz164ws-standard-laptop-intel-core-ultra-9-processor-285h32-gb1-tb-ssdintel-arc-graphicswindows-11msofficeoled-3556-cm-14-inch-ponder-blue-m8cyea-8977756",
    
    ("Apple iPad Air", "Amazon"):
        "https://www.amazon.in/Apple-iPad-Air-27-59-11%E2%80%B3/dp/B0GQVHBK9M?th=1",
    
    ("Apple iPad Air", "Flipkart"):
        "https://www.flipkart.com/apple-2024-ipad-air-m2-128-gb-rom-13-0-inch-wi-fi-only-m2-chip-blue/p/itmb01fe44a7923b?pid=TABHYZDZTHR7AWDH&lid=LSTTABHYZDZTHR7AWDHMDDMW6&marketplace=FLIPKART&store=tyy%2Fhry&srno=b_1_1&otracker=browse&fm=organic&iid=c04bdf01-947b-4bfe-b34b-6b5741fe9b7a.TABHYZDZTHR7AWDH.SEARCH&ppt=sp&ppn=productListView&ssid=s1bo3bqkf40000001782041373458&ov_redirect=true",
    
    ("Apple iPad Air", "Apple Store"):
        "https://www.amazon.in/Apple-iPad-Air-27-59-11%E2%80%B3/dp/B0GQVHBK9M?th=1",
    
    ("Apple iPad Pro", "Amazon"):
        "https://www.amazon.in/Apple-iPad-Pro-13%E2%80%B3-M5/dp/B0FWD431KF",
    
    ("Apple iPad Pro", "Flipkart"):
        "https://www.flipkart.com/apple-2022-ipad-pro-6th-gen-1-tb-rom-12-9-inch-wi-fi-only-m2-chip-silver/p/itm12927a2b88d55?pid=TABGJ6XUHHSRAWBV&lid=LSTTABGJ6XUHHSRAWBVVIQXP7&marketplace=FLIPKART&store=tyy%2Fhry&srno=b_1_1&otracker=browse&fm=organic&iid=616a3c56-8826-46f9-9190-dd8d737a60bb.TABGJ6XUHHSRAWBV.SEARCH&ppt=sp&ppn=productListView&ssid=qzripjy8kg0000001782041567394&ov_redirect=true",
    
    ("Apple iPad Pro", "Apple Store"):
        "https://www.apple.com/in/shop/buy-ipad/ipad-pro",
    
    ("Samsung Galaxy Tab S10+", "Amazon"):
        "https://www.amazon.in/Samsung-Dynamic-Display-Storage-Platinum/dp/B0DHHB2YS7",
    
    ("Samsung Galaxy Tab S10+", "Flipkart"):
        "https://www.flipkart.com/samsung-galaxy-tab-s10-12-gb-ram-256-rom-12-4-inch-wi-fi-only-gaming-tablet-platinum-silver/p/itm07fddd91caecf",
    
    ("Samsung Galaxy Tab S10+", "Croma"):
        "https://www.croma.com/samsung-galaxy-tab-s10-plus-wi-fi+5g-android-tablet-with-samsung-stylus-s-12-4-inch-12gb-ram-256gb-rom-moonstone-gray-/p/311506?srsltid=AfmBOorxXGFqchi1bAUjrQyDsplU6hl49q0ESH-lkoH2OkDs9kEEUREC",
    
    ("Samsung Galaxy Tab S10+", "Reliance Digital"):
        "https://www.reliancedigital.in/product/samsung-tab-s10-3149-cm-124-inch-wifi-tablet-with-s-pen-12-gb-ram-256-gb-silver-x820na-m1qhxy-8643323",
    
    ("Google Pixel Tablet", "Amazon"):
        "https://www.amazon.in/Google-Pixel-Tablet-Standalone-Porcelain/dp/B0CZMFZMR8?th=1",
    
    ("Google Pixel Tablet", "Flipkart"):
        "https://flipkart.com/google-pixel-tablet"
    
}





def fetch_products():
    """
    Fetches all products from the database    
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            p. product_id,
            b. brand_name,
            p. product_name
        FROM 
            products p
        JOIN brands b
        ON p.brand_id = b.brand_id;
    """
    cursor.execute(query)
    products = cursor.fetchall()

    cursor.close()
    connection.close()    

    return products



def fetch_stores():
    """
    Fetches all stores from the database    
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            store_id,
            store_name
        FROM 
            stores;
    """
    cursor.execute(query)
    stores = cursor.fetchall()

    cursor.close()
    connection.close()

    return stores



def generate_product_url(store_name, product_name):

     """
        Generates a product URL for the given store and product.
        Returns a real URL if available; otherwise generates a placeholder URL.
     """
     
     # Return real URL if available
     if (product_name, store_name) in PRODUCT_URL_MAPPING:
        return PRODUCT_URL_MAPPING[(product_name, store_name)]
     
     # Otherwise generate a placeholder URL
     slug = (
         product_name
         .lower()
         .replace(" ", "-")
         .replace("(", "")
         .replace(")", "")
     )

     domains = {
         "Amazon": "amazon.in",
         "Flipkart": "flipkart.com",
         "Croma": "croma.com",
         "Reliance Digital": "reliancedigital.in",
         "Vijay Sales": "vijaysales.com",
         "Apple Store": "apple.com/in/store"
     }

     return f"https://{domains[store_name]}/{slug}"



def generate_product_listings(products, stores):
    """
    Generates retailer product listings.
    """

    listings = []

    # Creating lookup dictionary
    store_lookup = {
        store["store_name"]:store["store_id"]
        for store in stores
    }

    for product in products:
        allowed_stores = STORE_MAPPING[product["brand_name"]]
        
        for store_name in allowed_stores:
            listing = {
                "product_id": product["product_id"],
                "store_id": store_lookup[store_name],
                "retailer_product_name": product["product_name"],
                "product_url": generate_product_url(store_name, product["product_name"]),
                "listing_status": "Active" 
            }
            
            listings.append(listing)

    return listings


def product_listings_exist():
    """ 
    Checks whether product listings already exist in the database. 
    """
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT COUNT(*)
        FROM product_listings;    
    """

    cursor.execute(query)

    count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return count > 0

def insert_product_listings(listings):
    """ 
    Inserts generated product listings into the database. 
    """
    
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO product_listings(
            product_id, 
            store_id, 
            retailer_product_name, 
            product_url, 
            listing_status
        )
        VALUES(%s, %s, %s, %s, %s)
    """
    values = [
        (
            listing["product_id"], 
            listing["store_id"], 
            listing["retailer_product_name"], 
            listing["product_url"], 
            listing["listing_status"]
        )
        for listing in listings
    ]

    cursor.executemany(query, values)

    connection.commit()
    
    print(f"Successfully inserted {len(values)} product listings.")

    cursor.close()
    connection.close()



def main():

    if product_listings_exist():
        print("Product listings already exist Skipping generation")
        return


    products = fetch_products()
    stores = fetch_stores()
    listings = generate_product_listings(products, stores)
    insert_product_listings(listings) 
    


if __name__ == "__main__":
    main()

