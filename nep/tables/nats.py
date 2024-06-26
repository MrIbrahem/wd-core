#!/usr/bin/env python3
"""
from nep.tables.nats import nationalities
"""

nationalities = {
    "آيسلندا": {"man": "آيسلندي", "women": "آيسلندية"},
    "ميانمار": {"man": "ميانماري", "women": "ميانمارية"},
    "الدولة الأموية": {"man": "أموي", "women": "أموية"},
    "الدولة العثمانية": {"man": "عثماني", "women": "عثمانية"},
    "مقدونيا الشمالية": {"man": "شمال مقدوني", "women": "شمال مقدونية"},
    "شمال مقدونيا": {"man": "شمال مقدوني", "women": "شمال مقدونية"},
    "مقدونيا القديمة": {"man": "مقدوني قديم", "women": "مقدونية قديمة"},
    "مقدونيا": {"man": "مقدوني", "women": "مقدونية"},
    "تركمان": {"man": "تركماني", "women": "تركمانية"},
    "تركمانستان": {"man": "تركماني", "women": "تركمانية"},
    "الإمبراطورية الرومانية المقدسة": {"man": "روماني مقدس", "women": "رومانية مقدسة"},
    "الإمبراطورية البيزنطية": {"man": "بيزنطي", "women": "بيزنطية"},
    "الإمبراطورية الساسانية": {"man": "ساساني", "women": "ساسانية"},
    "روما القديمة": {"man": "رومي قديم", "women": "رومية قديمة"},
    "رومانيا القديمة": {"man": "روماني قديم", "women": "رومانية قديمة"},
    "اليونان القديمة": {"man": "يوناني قديم", "women": "يونانية قديمة"},
    "الإمبراطورية النمساوية المجرية": {"man": "نمساوي مجري", "women": "نمساوية مجرية"},
    "الولايات المتحدة": {"man": "أمريكي", "women": "أمريكية"},
    "غوام": {"man": "غوامي", "women": "غوامية"},
    "ساموا الأمريكية": {"man": "ساموي أمريكي", "women": "ساموية أمريكية"},
    "بورتوريكو": {"man": "بورتوريكي", "women": "بورتوريكية"},
    "جزر سليمان": {"man": "سليماني", "women": "سليمانية"},
    "جزر القمر": {"man": "قمري", "women": "قمرية"},
    "تشيكوسلوفاكيا": {"man": "تشيكوسلوفاكي", "women": "تشيكوسلوفاكية"},
    "الرأس الأخضر": {"man": "رأس أخضري", "women": "رأس أخضرية"},
    "جزر الأنتيل": {"man": "أنتيلي", "women": "أنتيلية"},
    "البنغال": {"man": "بنغالي", "women": "بنغالية"},
    "بوهيميا": {"man": "بوهيمي", "women": "بوهيمية"},
    "جمهورية أفريقيا الوسطى": {"man": "أفريقي أوسطي", "women": "وسط أفريقية"},
    "القرم": {"man": "قرمي", "women": "قرمية"},
    "غينيا الاستوائية": {"man": "غيني استوائي", "women": "غينية استوائية"},
    "جزر فارو": {"man": "فاروي", "women": "فاروية"},
    "غويانا الفرنسية": {"man": "غوياني فرنسي", "women": "غويانية فرنسية"},
    "قيرغيز": {"man": "قيرغيزي", "women": "قيرغيزية"},
    "مورافيا": {"man": "مورافي", "women": "مورافية"},
    "دول الشمال": {"man": "نوردي", "women": "نوردية"},
    "أوسيتيا الجنوبية": {"man": "أوسيتي", "women": "أوسيتية"},
    "جنوب شرق آسيا": {"man": "آسيوي جنوب شرقي", "women": "آسيوية جنوب شرقية"},
    "أوروبا الجنوبية": {"man": "أوروبي جنوبي", "women": "أوروبية جنوبية"},
    "جنوب غرب آسيا": {"man": "جنوب غرب آسيوي", "women": "جنوب غربي آسيوية"},
    "ترينيداد وتوباغو": {"man": "ترنيدادي", "women": "ترنيدادية"},
    "الهند الغربية": {"man": "هندي غربي", "women": "هندية غربية"},
    "يوروبا": {"man": "يوروبي", "women": "يوروبية"},
    "الأبالاش": {"man": "أبلاشي", "women": "أبلاشية"},
    "أسترالاسيا": {"man": "أسترالاسي", "women": "أسترالاسية"},
    "آسيا الوسطى": {"man": "آسيوي أوسطي", "women": "آسيوية أوسطية"},
    "الشيشان": {"man": "شيشاني", "women": "شيشانية"},
    "تايبيه الصينية": {"man": "تايبي صيني", "women": "تايبيه صينية"},
    "شرق آسيا": {"man": "آسيوي شرقي", "women": "آسيوية شرقية"},
    "ولايات ميكرونيسيا المتحدة": {"man": "ميكرونيزي", "women": "ميكرونيزية"},
    "غوادلوب": {"man": "غواديلوبي", "women": "غواديلوبية"},
    "قبرص الشمالية": {"man": "قبرصي شمالي", "women": "قبرصية شمالية"},
    "ناورو": {"man": "ناوروني", "women": "ناورونية"},
    "غامبيا": {"man": "غامبي", "women": "غامبية"},
    "الاتحاد السوفيتي": {"man": "سوفيتي", "women": "سوفيتية"},
    "غرب آسيا": {"man": "آسيوي غربي", "women": "آسيوية غربية"},
    "الصحراء الغربية": {"man": "صحراوي", "women": "صحراوية"},
    "ماكاو": {"man": "ماكاوي", "women": "ماكاوية"},
    "زائير": {"man": "زائيري", "women": "زائيرية"},
    "المملكة المتحدة": {"man": "بريطاني", "women": "بريطانية"},
    "جورجيا": {"man": "جورجي", "women": "جورجية"},
    "الشرق الأوسط": {"man": "شرق أوسطي", "women": "شرقية أوسطية"},
    "الأوروغواي": {"man": "أوروغواياني", "women": "أوروغوايانية"},
    "جبل طارق": {"man": "جبل طارقي", "women": "جبل طارقية"},
    "رودسيا": {"man": "رودوسي", "women": "رودوسية"},
    "جزر مارشال": {"man": "مارشالي", "women": "مارشالية"},
    "الصين": {"man": "صيني", "women": "صينية"},
    "أيرلندا الشمالية": {"man": "أيرلندي شمالي", "women": "أيرلندية شمالية"},
    "أيرلندا": {"man": "أيرلندي", "women": "أيرلندية"},
    "جمهورية أيرلندا": {"man": "أيرلندي", "women": "أيرلندية"},
    "اسكتلندا": {"man": "اسكتلندي", "women": "اسكتلندية"},
    "إنجلترا": {"man": "إنجليزي", "women": "إنجليزية"},
    "ويلز": {"man": "ويلزي", "women": "ويلزية"},
    "أبخازيا": {"man": "أبخازي", "women": "أبخازية"},
    "أفغانستان": {"man": "أفغاني", "women": "أفغانية"},
    "أفريقيا": {"man": "أفريقي", "women": "أفريقية"},
    "ألبانيا": {"man": "ألباني", "women": "ألبانية"},
    "الجزائر": {"man": "جزائري", "women": "جزائرية"},
    "مصر القديمة": {"man": "مصري قديم", "women": "مصرية قديمة"},
    "إغريق": {"man": "إغريقي", "women": "إغريقية"},
    "الأندلس": {"man": "أندلسي", "women": "أندلسية"},
    "أندورا": {"man": "أندوري", "women": "أندورية"},
    "أنغولا": {"man": "أنغولي", "women": "أنغولية"},
    "الأرجنتين": {"man": "أرجنتيني", "women": "أرجنتينية"},
    "أرمينيا": {"man": "أرميني", "women": "أرمينية"},
    "آسيا": {"man": "آسيوي", "women": "آسيوية"},
    "أستراليا": {"man": "أسترالي", "women": "أسترالية"},
    "النمسا": {"man": "نمساوي", "women": "نمساوية"},
    "أذربيجان": {"man": "أذربيجاني", "women": "أذربيجانية"},
    "باهاماس": {"man": "باهاماسي", "women": "باهاماسية"},
    "البحرين": {"man": "بحريني", "women": "بحرينية"},
    "بنغلاديش": {"man": "بنغلاديشي", "women": "بنغلاديشية"},
    "باربادوس": {"man": "باربادوسي", "women": "باربادوسية"},
    "روسيا البيضاء": {"man": "بيلاروسي", "women": "بيلاروسية"},
    "بلجيكا": {"man": "بلجيكي", "women": "بلجيكية"},
    "بليز": {"man": "بليزي", "women": "بليزية"},
    "بنين": {"man": "بنيني", "women": "بنينية"},
    "بوتان": {"man": "بوتاني", "women": "بوتانية"},
    "بوليفيا": {"man": "بوليفي", "women": "بوليفية"},
    "البوسنة والهرسك": {"man": "بوسني", "women": "بوسنية"},
    "بوتسوانا": {"man": "بوتسواني", "women": "بوتسوانية"},
    "البرازيل": {"man": "برازيلي", "women": "برازيلية"},
    "بلغاريا": {"man": "بلغاري", "women": "بلغارية"},
    "بوركينا فاسو": {"man": "بوركينابي", "women": "بوركينابية"},
    "بوروندي": {"man": "بوروندي", "women": "بوروندية"},
    "كمبوديا": {"man": "كمبودي", "women": "كمبودية"},
    "الكاميرون": {"man": "كاميروني", "women": "كاميرونية"},
    "كندا": {"man": "كندي", "women": "كندية"},
    "الكاريبي": {"man": "كاريبي", "women": "كاريبية"},
    "تشاد": {"man": "تشادي", "women": "تشادية"},
    "تشيلي": {"man": "تشيلي", "women": "تشيلية"},
    "كولومبيا": {"man": "كولومبي", "women": "كولومبية"},
    "كوستاريكا": {"man": "كوستاريكي", "women": "كوستاريكية"},
    "كرواتيا": {"man": "كرواتي", "women": "كرواتية"},
    "كوبا": {"man": "كوبي", "women": "كوبية"},
    "قبرص": {"man": "قبرصي", "women": "قبرصية"},
    "التشيك": {"man": "تشيكي", "women": "تشيكية"},
    "الدنمارك": {"man": "دنماركي", "women": "دنماركية"},
    "جيبوتي": {"man": "جيبوتي", "women": "جيبوتية"},
    "جمهورية الدومنيكان": {"man": "دومينيكاني", "women": "دومينيكانية"},
    "جمهورية الدومينيكان": {"man": "دومينيكاني", "women": "دومينيكانية"},
    "تيمور الشرقية": {"man": "تيموري شرقي", "women": "تيمورية شرقية"},
    "الإكوادور": {"man": "إكوادوري", "women": "إكوادورية"},
    "مصر": {"man": "مصري", "women": "مصرية"},
    "السلفادور": {"man": "سلفادوري", "women": "سلفادورية"},
    "إريتريا": {"man": "إريتري", "women": "إريترية"},
    "إستونيا": {"man": "إستوني", "women": "إستونية"},
    "إسواتيني": {"man": "إسواتيني", "women": "إسواتينية"},
    "إثيوبيا": {"man": "إثيوبي", "women": "إثيوبية"},
    "أوروبا": {"man": "أوروبي", "women": "أوروبية"},
    "فيجي": {"man": "فيجي", "women": "فيجية"},
    "فنلندا": {"man": "فنلندي", "women": "فنلندية"},
    "فرنسا": {"man": "فرنسي", "women": "فرنسية"},
    "الغابون": {"man": "غابوني", "women": "غابونية"},
    "ألمانيا": {"man": "ألماني", "women": "ألمانية"},
    "غانا": {"man": "غاني", "women": "غانية"},
    "اليونان": {"man": "يوناني", "women": "يونانية"},
    "جرينلاند": {"man": "جرينلاندي", "women": "جرينلاندية"},
    "غرينادا": {"man": "غرينادي", "women": "غرينادية"},
    "غواتيمالا": {"man": "غواتيمالي", "women": "غواتيمالية"},
    "غينيا": {"man": "غيني", "women": "غينية"},
    "بابوا غينيا الجديدة": {"man": "غيني", "women": "غينية"},
    "غينيا بيساو": {"man": "غيني بيساوي", "women": "غينية بيساوية"},
    "غيانا": {"man": "غياني", "women": "غيانية"},
    "هايتي": {"man": "هايتي", "women": "هايتية"},
    "هندوراس": {"man": "هندوراسي", "women": "هندوراسية"},
    "هونغ كونغ": {"man": "هونغ كونغي", "women": "هونغ كونغية"},
    "المجر": {"man": "مجري", "women": "مجرية"},
    "الهند": {"man": "هندي", "women": "هندية"},
    "إندونيسيا": {"man": "إندونيسي", "women": "إندونيسية"},
    "إيران": {"man": "إيراني", "women": "إيرانية"},
    "العراق": {"man": "عراقي", "women": "عراقية"},
    "إسرائيل": {"man": "إسرائيلي", "women": "إسرائيلية"},
    "جزر فيرجن البريطانية": {"man": "فيرجني", "women": "فيرجنية"},
    "برمودا": {"man": "برمودي", "women": "برمودية"},
    "موناكو": {"man": "موناكي", "women": "موناكية"},
    "بروناي": {"man": "بروني", "women": "برونية"},
    "كاليدونيا الجديدة": {"man": "كاليدوني", "women": "كاليدونية"},
    "إيطاليا": {"man": "إيطالي", "women": "إيطالية"},
    "ساحل العاج": {"man": "إفواري", "women": "إفوارية"},
    "جامايكا": {"man": "جامايكي", "women": "جامايكية"},
    "اليابان": {"man": "ياباني", "women": "يابانية"},
    "الأردن": {"man": "أردني", "women": "أردنية"},
    "يهود": {"man": "يهودي", "women": "يهودية"},
    "كازاخستان": {"man": "كازاخستاني", "women": "كازاخستانية"},
    "كينيا": {"man": "كيني", "women": "كينية"},
    "كيريباتي": {"man": "كيريباتي", "women": "كيريباتية"},
    "كوريا": {"man": "كوري", "women": "كورية"},
    "كوسوفو": {"man": "كوسوفي", "women": "كوسوفية"},
    "الكويت": {"man": "كويتي", "women": "كويتية"},
    "قيرغيزستان": {"man": "قيرغيزستاني", "women": "قيرغيزستانية"},
    "بروسيا": {"man": "بروسي", "women": "بروسية"},
    "لاوس": {"man": "لاوسي", "women": "لاوسية"},
    "لاتفيا": {"man": "لاتيفي", "women": "لاتيفية"},
    "لبنان": {"man": "لبناني", "women": "لبنانية"},
    "ليسوتو": {"man": "ليسوثوي", "women": "ليسوثوية"},
    "ليبيريا": {"man": "ليبيري", "women": "ليبيرية"},
    "ليبيا": {"man": "ليبي", "women": "ليبية"},
    "ليختنشتاين": {"man": "ليختنشتاني", "women": "ليختنشتانية"},
    "ليتوانيا": {"man": "ليتواني", "women": "ليتوانية"},
    "لوكسمبورغ": {"man": "لوكسمبورغي", "women": "لوكسمبورغية"},
    "مدغشقر": {"man": "مدغشقري", "women": "مدغشقرية"},
    "مالاوي": {"man": "ملاوي", "women": "ملاوية"},
    "ماليزيا": {"man": "ماليزي", "women": "ماليزية"},
    "جزر المالديف": {"man": "مالديفي", "women": "مالديفية"},
    "مالي": {"man": "مالي", "women": "مالية"},
    "مالطا": {"man": "مالطي", "women": "مالطية"},
    "موريتانيا": {"man": "موريتاني", "women": "موريتانية"},
    "موريشيوس": {"man": "موريشيوسي", "women": "موريشيوسية"},
    "المكسيك": {"man": "مكسيكي", "women": "مكسيكية"},
    "مولدوفا": {"man": "مولدوفي", "women": "مولدوفية"},
    "منغوليا": {"man": "منغولي", "women": "منغولية"},
    "الجبل الأسود": {"man": "مونتينيغري", "women": "مونتينيغرية"},
    "المغرب": {"man": "مغربي", "women": "مغربية"},
    "موزمبيق": {"man": "موزمبيقي", "women": "موزمبيقية"},
    "ناميبيا": {"man": "ناميبي", "women": "ناميبية"},
    "نيبال": {"man": "نيبالي", "women": "نيبالية"},
    "هولندا": {"man": "هولندي", "women": "هولندية"},
    "نيوزيلندا": {"man": "نيوزيلندي", "women": "نيوزيلندية"},
    "نيكاراغوا": {"man": "نيكاراغوي", "women": "نيكاراغوية"},
    "النيجر": {"man": "نيجري", "women": "نيجرية"},
    "نيجيريا": {"man": "نيجيري", "women": "نيجيرية"},
    "كوريا الشمالية": {"man": "كوري شمالي", "women": "كورية شمالية"},
    "النرويج": {"man": "نرويجي", "women": "نرويجية"},
    "أوقيانوسيا": {"man": "أوقيانوسي", "women": "أوقيانوسية"},
    "عمان": {"man": "عماني", "women": "عمانية"},
    "باكستان": {"man": "باكستاني", "women": "باكستانية"},
    "بالاو": {"man": "بالاوي", "women": "بالاوية"},
    "فلسطين": {"man": "فلسطيني", "women": "فلسطينية"},
    "بنما": {"man": "بنمي", "women": "بنمية"},
    "باراغواي": {"man": "باراغواياني", "women": "باراغوايانية"},
    "بيرو": {"man": "بيروي", "women": "بيروية"},
    "الفلبين": {"man": "فلبيني", "women": "فلبينية"},
    "بولندا": {"man": "بولندي", "women": "بولندية"},
    "البرتغال": {"man": "برتغالي", "women": "برتغالية"},
    "قطر": {"man": "قطري", "women": "قطرية"},
    "جمهورية الكونغو": {"man": "كونغوي", "women": "كونغوية"},
    "جمهورية الكونغو الديمقراطية": {
        "man": "كونغوي ديمقراطي",
        "women": "كونغوية ديمقراطية",
    },
    "رومانيا": {"man": "روماني", "women": "رومانية"},
    "روسيا": {"man": "روسي", "women": "روسية"},
    "رواندا": {"man": "رواندي", "women": "رواندية"},
    "ساموا": {"man": "ساموي", "women": "ساموية"},
    "السعودية": {"man": "سعودي", "women": "سعودية"},
    "السنغال": {"man": "سنغالي", "women": "سنغالية"},
    "صربيا": {"man": "صربي", "women": "صربية"},
    "سيشل": {"man": "سيشلي", "women": "سيشلية"},
    "سيراليون": {"man": "سيراليوني", "women": "سيراليونية"},
    "سنغافورة": {"man": "سنغافوري", "women": "سنغافورية"},
    "سلوفاكيا": {"man": "سلوفاكي", "women": "سلوفاكية"},
    "سلوفينيا": {"man": "سلوفيني", "women": "سلوفينية"},
    "الصومال": {"man": "صومالي", "women": "صومالية"},
    "جنوب أفريقيا": {"man": "جنوب أفريقي", "women": "جنوب أفريقية"},
    "كوريا الجنوبية": {"man": "كوري جنوبي", "women": "كورية جنوبية"},
    "جنوب السودان": {"man": "جنوب سوداني", "women": "جنوبية سودانية"},
    "إسبانيا": {"man": "إسباني", "women": "إسبانية"},
    "سريلانكا": {"man": "سريلانكي", "women": "سريلانكية"},
    "السودان": {"man": "سوداني", "women": "سودانية"},
    "سورينام": {"man": "سورينامي", "women": "سورينامية"},
    "سوازيلاند": {"man": "سوازيلندي", "women": "سوازيلندية"},
    "السويد": {"man": "سويدي", "women": "سويدية"},
    "سويسرا": {"man": "سويسري", "women": "سويسرية"},
    "سوريا": {"man": "سوري", "women": "سورية"},
    "ساو تومي": {"man": "ساوتومي", "women": "ساوتومية"},
    "تايوان": {"man": "تايواني", "women": "تايوانية"},
    "طاجيكستان": {"man": "طاجيكي", "women": "طاجيكستانية"},
    "تنزانيا": {"man": "تنزاني", "women": "تنزانية"},
    "تايلاند": {"man": "تايلاندي", "women": "تايلاندية"},
    "توغو": {"man": "توغوي", "women": "توغوية"},
    "تونغا": {"man": "تونغاني", "women": "تونغانية"},
    "تونس": {"man": "تونسي", "women": "تونسية"},
    "تركيا": {"man": "تركي", "women": "تركية"},
    "توفالو": {"man": "توفالي", "women": "توفالية"},
    "أوغندا": {"man": "أوغندي", "women": "أوغندية"},
    "أوكرانيا": {"man": "أوكراني", "women": "أوكرانية"},
    "الإمارات": {"man": "إماراتي", "women": "إماراتية"},
    "أوزبكستان": {"man": "أوزبكستاني", "women": "أوزبكستانية"},
    "فانواتو": {"man": "فانواتي", "women": "فانواتية"},
    "الفاتيكان": {"man": "فاتيكاني", "women": "فاتيكانية"},
    "فنزويلا": {"man": "فنزويلي", "women": "فنزويلية"},
    "فيتنام": {"man": "فيتنامي", "women": "فيتنامية"},
    "اليمن": {"man": "يمني", "women": "يمنية"},
    "يوغوسلافيا": {"man": "يوغوسلافي", "women": "يوغوسلافية"},
    "زامبيا": {"man": "زامبي", "women": "زامبية"},
    "زيمبابوي": {"man": "زيمبابوي", "women": "زيمبابوية"},
    "أمريكا الوسطى": {"man": "أمريكي أوسطي", "women": "أمريكية أوسطية"},
    "أمريكا الشمالية": {"man": "أمريكي شمالي", "women": "أمريكية شمالية"},
    "أمريكا الجنوبية": {"man": "أمريكي جنوبي", "women": "أمريكية جنوبية"},
    "فيكتوريا (أستراليا)": {"man": "فيكتوري", "women": "فيكتورية"},
}
# ---
