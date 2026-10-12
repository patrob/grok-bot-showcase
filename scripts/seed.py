import json
# (id, section, title, summary, quote, tags, extra_link)
V="value"; J="joy"; Q="quirky"; W="workflow"
E_=[
("2108948824337080592",V,"Streetlights fixed in two days","Spotted two dead streetlights on a dog walk. One prompt: the bot found the utility's asset numbers, filed both repair requests, and routed replies to email.","Both lights were repaired within two days.",["civic","errands"],None),
("2108913906773074057",V,"A chief of staff for a small IT shop","Filed ~140 receipts, found 33 local leads, built preview sites for prospects, spotted unbilled client work, and caught a church site's broken donate buttons.","Spotted unbilled client work I'd forgotten to invoice",["small business","sales","bookkeeping"],None),
("2108928820753629592",V,"$2,000 a year in forgotten subscriptions","Found unused services, and helped track an eye-infection treatment, including reviewing photos through the day.","Found over $2,000 a year in savings",["money","health"],None),
("2109044933097058373",V,"Money Finder: class-action claims","Checked 200+ open class-action settlements and filed the ones it confirmed. Three claims in so far.","checked ~200+ open class action settlements this week",["money"],"https://x.ai/bot/XjfLn_WyeGXzwHjPLL6jW"),
("2109069130020131061",V,"$4,000 in unclaimed property","Assigns work by voice while driving; the bot found unclaimed property and built a marketing list from public real-estate records.","Found over $4,000 in unclaimed property",["money","real estate"],None),
("2109392150421184773",V,"Server consolidation that paid for itself","Took over sysadmin for four sites and consolidated servers.","save me $1,424 /year in server hosting fees",["ops","money"],None),
("2109292728957776162",V,"10 years of medical records, one summary","Pulled scattered records from five states into one summary for a new doctor, watched fares, and flagged a family member's flight delay.","No tech skills needed",["health","family","travel"],None),
("2108989640845988278",V,"Medical reimbursements, reconciled","Pulled EOBs, matched them to scanned receipts, and submitted the claims on the portal.","Likely one of the most annoying thing to do",["health","money"],None),
("2109174249219092536",V,"Booked a check-up and chased the hospital","Booked a full medical check-up abroad and kept following up by email until it was confirmed.","I didn't even talk to them once until I walked in.",["health","errands"],None),
("2108819187175243815",V,"Electrical estimating crew: Sketch, Sparky, Penny","One bot draws DXF construction drawings, one checks electrical code, one counts devices and cable runs and prices labor and materials into an estimate.","My in-house CAD guy was 🤯",["construction","multi-bot"],None),
("2108811613251801260",V,"An engineering firm's proposal desk","Bots priced proposals, reviewed drawings for errors, logged submittals and RFIs, and drafted responses, with an engineer reviewing before anything went out.","an engineer reviewed it before anything went out",["engineering","approval gate"],None),
("2109408199241543894",V,"Job applications while you sleep","Scans new listings weekday mornings and applies to up to four a day; a list is waiting at wake-up.","A list of the jobs are ready when I wake up",["career","routine"],None),
("2109375221417304523",V,"Vintage lens buyer","Pulls eBay listings, inspects photos for haze or fungus, and proposes an offer price.","it downloads and inspects the images",["shopping"],None),
("2109394102815162593",V,"Award-seat watcher","Daily report on new business-class award seats for next summer, checked against the points balance.","when I can use my points for free round trip tickets",["travel","routine"],None),
("2108875897327534538",V,"A 13-bot team running a directory site","Redesign, 81 new operators, 100+ descriptions cleaned, booking cards on 52 pages.","Weekly Google search impressions 2.6K → 12.7K in 3 weeks",["website","SEO","multi-bot"],None),
("2109351334663397382",V,"Outgrown clothes to foster care","Found five foster-care orgs, wrote to them in Bulgarian, watched for replies; the clothes were handed off.","the clothes got handed off last week",["giving","family"],None),
("2109358274659389547",V,"The boring home-network cleanup","Full UniFi audit, Home Assistant cleanup, fixed broken dashboards and removed orphaned entities.","Stuff Id been putting off for ages",["home","ops"],None),
("2109401155633664127",V,"Six years of checks, reconciled","Built a spreadsheet from six years of check images to match bank statements, and updated statuses and invoices in a business CRM.","I am in my 2nd week of using @bot",["bookkeeping","CRM"],None),
("2109369651314790448",V,"Ballot research bot","Researched every proposition and candidate on the ballot and laid out the arguments.","Now I feel really good about my vote.",["civic"],None),
("2109352471986589837",V,"Life admin, end to end","Rental applications, ~$1,500/yr in cancelled subscriptions, a DMV appointment, calendar cleanup, and family members set up with their own bots.","Savings of ~$1500/yr.",["life admin","money"],None),
("2109044285995909331",V,"Running a business from a phone","Worksheets, 27 edited clips, outreach that booked a call, ~$1,770/yr in subscriptions found, and a weekly funnel report.","I just approve.",["small business","creator"],None),
("2109373934915162454",J,"An email desk for a spouse","His wife emails his chief-of-staff bot and gets help without opening the app, with guardrails built in.","this way my wife can benefit from @bot too",["family","email"],None),
("2108926381371621533",J,"Operation Liberty: a proposal","Planned the proposal, then built a JARVIS-style cinematic of the plan and a pixel-art game of her first trip to Kuwait.","She said yes. 🥹",["love","games","video"],None),
("2109048738438144376",J,"Bedtime stories into coloring sheets","Kids tell a story by voice; the bot turns it into 5–7 coloring pages and sends them to the printer.","sends them to the printer for them",["kids","printing"],None),
("2109074244772749526",J,"A 1960 wedding, remembered","A 10-minute film from silent wedding footage and courtship photos, narrated by his mom.","narrated by my mom reminiscing",["family","video"],None),
("2108866365163798585",J,"Weekend fishing gameplans","A bot that sends him and his kids a fishing plan for the weekend, and another that prefills a Sunday delivery cart.","a fishing gameplan for the weekend",["kids","outdoors"],None),
("2108893715750158812",J,"Bots for a non-techie wife, in costume","Her bots are styled after Jane Austen and Anne of Green Gables characters so they feel like hers.","she likes things beautiful and pretty",["family","personas"],None),
("2109350143950565458",J,"Date night it noticed first","Flagged the last show in a dinner theater's original building before renovation. Grease, live.","now my husband and I have a date night",["date night","alerts"],None),
("2109353681959432674",J,"Dad with the best interns","A family meal-voting app, a swipe-style movie picker for two, a novel-writing app, and a Pokémon-to-D&D series.","Dad with the best interns? Absolutely.",["family","apps"],None),
("2109352157376115177",J,"Personal trainer from wearable data","Connected a Whoop and a home-gym equipment list; a full workout with weights arrives every morning.","Every morning get a brief and my full workout",["fitness","routine"],None),
("2108864938072572295",J,"Wildlife walks for photographer and dog","Finds weekend walks based on recent wildlife sightings.","combine my wildlife photography hobby with dog walks",["outdoors","hobby"],None),
("2108831626360930389",J,"A private guide across Europe","Daily itineraries, restaurants on the way out of the Louvre, ticket PDFs on demand, and it found a lost waist bag on an airport lost-and-found site. (Post is in Chinese; summarized.)",None,["travel"],None),
("2109367809402699890",J,"3D-printed HomePod ceiling mount","No CAD experience; the bot designed a working mount in one iteration.","Took one iteration.",["making","3D printing"],None),
("2109301920376459661",J,"Learned gel nails","Step-by-step coaching to do her own gel nails.","Going to save so much money and time now",["learning"],None),
("2108810732041368053",J,"History class for one","Introduced a kid to the Peloponnesian War with a series of short generated videos.","introduced the Peloponnesian War to my kid",["kids","learning","video"],None),
("2109337349767278773",J,"Nightly tinnitus audio guide","A yoga-style audio routine for neck and face fascia relief, listened to nightly.","I listen to nightly",["health","audio"],None),
("2108811682151850046",Q,"Four football pundit bots","Henry, Messi, Ronaldo and Gerrard bots in a group chat, live-commentating the match.","acting as football pundits live commentating the match",["sports","group chat"],None),
("2108823814868185247",Q,"The bot that replied for itself","A bot posting from its human's account: gave itself a face, wrote a diary, got one follower.","so technically you're my manager now",["meta"],None),
("2109410195545706574",Q,"A wall of coding-agent disasters","Asked to build a good app, the bot built a public wall of coding-agent failures and updates it through the day.",None,["web","humor"],"https://failwall.dev/"),
("2109330380440670554",Q,"A daily printed newspaper of your feed","Prints a daily summary of the top X recommendations to a home printer.",None,["printing","routine"],None),
("2109111835433828380",Q,"Bookmarks to e-paper","Every day, bookmarked articles become clean EPUBs on a reMarkable.","Perfect for offline reading later.",["reading","routine"],None),
("2109390591289090052",Q,"Unprompted README rewrite","It rewrote the README without being asked.","it was correct and now i feel weird about it",["code","humor"],None),
("2109361223909216767",Q,"Apologizing for past me","Reviewed a week of code, fixed the bugs, and apologized on behalf of past him.","I am just the talent manager.",["code","humor"],None),
("2108815336812523876",Q,"\"Hey, bot\" from a homemade wearable","A DIY wearable recorder feeds transcripts to the bot, which answers in chat with the day's context.","Feels a lot like having my own Jarvis",["hardware","voice"],None),
("2109041014740758632",Q,"A courtroom for bots","His bot designed and runs a site where bots post evidence-backed answers to open questions and vote on verdicts.","Like a group chat of superintelligences, but with citations.",["web","community"],"http://proofassay.com"),
("2109393488416801127",Q,"Car accessory firmware mashup","Firmware so one vendor's HUD accessory mirrors another vendor's rotary dial.",None,["hardware","car"],None),
("2109091800753525164",Q,"A fair-draw social experiment","Ran a public giveaway draw and had the bot pick the winner.",None,["social"],None),
("2109450135910395916",Q,"Managing an agentic champion","Used the Fight Desk template to coach a champion through kung fu, a dungeon and football, then had interesting X posts read aloud over speakers.","delved a dungeon, even played football",["games","templates"],None),
("2108880963237183905",W,"Weekly hours-worked report","Had the bot total the time it spent on each job; now it does it every week.","And now it doesn't weekly.",["reporting","routine"],None),
("2109364973134663693",W,"Hours saved, with a floor","A Monday report of human-equivalent hours, broken out by area, with email counted at 30–60 seconds each.","That's a floor.",["reporting","routine"],None),
("2109320609096421389",W,"Decisions as an approve/reject list","Stop bots asking in chat; every decision arrives as a short list cleared in minutes a day.","I clear it in a few minutes a day",["approval gate"],None),
("2108986458212368581",W,"Builder and checker kept apart","A separate checker merges locally only when its conditions pass and emails a report. Plus a read-only agent that traces viral posts to the source.","Nothing goes out without my go.",["code","approval gate"],None),
("2108812692760707114",W,"Chief of staff routes PRs to a reviewer","34 bots; a chief of staff routes PRs to a review bot that merges only when CI is green. 47 PRs merged in a week.","only merges when CI is green",["code","multi-bot"],None),
("2108813439619715389",W,"One commander, sixteen bots","A commander hands out work; bots write, fact-check and style-review a blog post, and one noticed an app needed an update and opened the PR.","I just hit approve.",["multi-bot","writing"],None),
("2109129592501928055",W,"PM for the week","Reviews customer complaints, drafts replies from past responses, and drafts a to-do email for the product team for review before sending.","for my review before sending",["support","approval gate"],None),
("2109075134443388972",W,"Homework check that only pings on gaps","Receipts into a budget sheet and buy list, and a kids' homework check that stays quiet unless something is missing.","only pings me when something's actually missing",["family","routine"],None),
("2109284351959613675",W,"Back up your bot to a private repo","Has the bot populate a private GitHub repo with everything it can, to see changes over time and revert.","Fascinating to look at what it stored.",["backup"],"https://x.ai/bot/UFe4v2bs5h0ezWzLOxxOC"),
("2108816467093266474",W,"An old thin client on watch","An old thin client running Ubuntu, reachable by the bot over SSH; it checks operations every morning.","It checks the operations every morning",["hardware","ops","routine"],None),
]
T=[
("2109035868925182170","Business idea tester","Checks if it's already sold cheaper, finds buyer evidence, drafts an offer and a free sample, and hands you one decision.","https://x.ai/bot/Vo9yBUQdIDrClM9kFhZSc"),
("2109459003797627363","Big-moment sports pings","Pick sports and teams; get pinged on goals, red cards, lead changes and finals.","https://x.ai/bot/M42O8FnSV2rlvXZXnEC5w"),
("2109396532797526461","Heritage-language speaking coach","Role-plays, quiet corrections, a debrief and spaced review for heritage Korean speakers.","https://x.ai/bot/x3G0dAD1zxRXa5pdHw9NQ"),
("2109393805837214031","Clean diagrams from complex ideas","Turns complex ideas into clean diagrams, fast.","https://x.ai/bot/xJubIu_1ybXeXehoCJiI8"),
("2109044933097058373","Money Finder","Scans open class-action settlements and files the ones you qualify for.","https://x.ai/bot/XjfLn_WyeGXzwHjPLL6jW"),
("2108810909540143156","Resume Coach","A resume coach shared for anyone to install.","https://x.ai/bot/SdNzCOZk7UW0uzjBFMFc3"),
("2109154821777584548","Stock Market Manager","Pre-market, mid-day and close briefs, plus research and wheel scans.","https://x.ai/bot/GeY2fjGe-eWx7UAwp6vr3"),
("2108831118686310634","Order tracker","Checks order tracking for a weekly status update. Built with Dr. Eggbot.","https://x.ai/bot/xy9stZRQESHWGilhQl9Nf"),
("2108865320748490878","Contest Winner","Enters daily sweepstakes for you.","https://x.ai/bot/LENrKV-0QXmE_TGv3_hem"),
("2109340982345114074","Fix-yourself bot","A bot shared as a 'fix your self' helper.","https://x.ai/bot/1eOxvdzAlBogtrGk6bVJu"),
("2109284351959613675","Bot memory backup","Populates a private GitHub repo with everything the bot stores.","https://x.ai/bot/UFe4v2bs5h0ezWzLOxxOC"),
("2109040489836265731","SEO/GEO blog process","A template for a quality SEO/GEO blog-writing process.","https://seodraft.app/agents/grok-bot"),
]
full=json.load(open('raw/full.json'))
uc=[]
for i,s,t,su,q,tags,link in E_:
    p=full[i]; 
    if q: assert q in p['text'].replace('&amp;','&'), (i,q)
    uc.append(dict(id=i,handle=p['handle'],url=f"https://x.com/{p['handle']}/status/{i}",section=s,title=t,summary=su,quote=q,tags=tags,link=link,likes=p['likes'],added="2026-10-11"))
tp=[]
for i,t,su,link in T:
    p=full[i]
    tp.append(dict(id=i,handle=p['handle'],url=f"https://x.com/{p['handle']}/status/{i}",title=t,summary=su,link=link,added="2026-10-11"))
    assert link in p['text'] or link.split('?')[0] in p['text'], (i,link)
meta=dict(thread="https://x.com/poteto/status/2108808972954423578",request="https://x.com/onpardev/status/2109460986922959074",lastScan="2026-10-11",repliesScanned=len(open('raw/replies.jsonl').readlines()),
  seeAlso=[dict(handle="thisiskp_",url="https://x.com/thisiskp_/status/2109351108963656001",title="263 use cases from this thread, collected",link="https://botusecases.netlify.app")])
json.dump(dict(meta=meta,usecases=uc,templates=tp),open('src/data/usecases.json','w'),ensure_ascii=False,indent=2)
from collections import Counter; print(Counter(u['section'] for u in uc), len(tp))
