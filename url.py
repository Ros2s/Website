import requests
import urllib.request
import random
from urllib.error import URLError, HTTPError

 # 设置代理，分为 http 和 https
proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }

user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/94.0.4606.61 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
    ]
headers = {
        'User-Agent': random.choice(user_agent)
    }
# 要检测的网站列表
websites = ['https://www.google.com', 'https://www.github.com', 'https://www.example.com','https://baidu.com','https://10ktf-shops.xyz',
'https://2023musk.io',
'https://2099nft.com',
'https://acrocalypses.xyz',
'https://apiwalletresolvenet.com',
'https://app-polkadot.com',
'https://appvalidation.online',
'https://bridge-polkadot.com',
'https://dappsapproval.com',
'https://dappsconnect.support',
'https://fastsmartsolution.netlify.app',
'https://hrshcryptz.live',
'https://iconnectwall.org',
'https://meerrgecoienvv2.xyz',
'https://nodesecureswap.com',
'https://resolve-portal-migrate.online',
'https://accountvalidation.in',
'https://activenodelaunch.site',
'https://air-secured.org',
'https://alaskacareusa.online',
'https://apps-linkup.co',
'https://aptoslab-dappstool.xyz',
'https://assetledgersecure.com',
'https://authenticatedapp.live',
'https://authenticationdapp.live',
'https://authydapps.live',
'https://babyapesclub.net',
'https://bbndapp.com',
'https://beta-defi.live',
'https://bip39seedsnodeservers.online',
'https://bitvalidate.online',
'https://blockdapp.net',
'https://buy-tamadoge.live',
'https://centralized-protocol.online',
'https://centralizedefinetworks.live',
'https://claim-bigeyes.com',
'https://coiemeergeev2.live',
'https://coinsolution-rectify.netlify.app',
'https://coinsteam.tech',
'https://connect-apps.tech',
'https://connect-collab.org',
'https://connect-wallect.netlify.app',
'https://connectnode.ml',
'https://connectwallet-vault.firebaseapp.com',
'https://connectwallet-vault.web.app',
'https://conneectiionfix.com',
'https://coreumlive.com',
'https://correctlonbot.com',
'https://dapps-secure.netlify.app',
'https://dapps2fa.link',
'https://dappsconfiguration.net',
'https://dappsolutions.github.io',
'https://dappssyn.glitch.me',
'https://dappwallet-con.square.site',
'https://dappwalletsupport.com',
'https://defichain-solutions.com',
'https://defiprotocol.support',
'https://dev-algo.online',
'https://devteamtools.org',
'https://dexconnectrectify.com',
'https://dexfix.site',
'https://diemjoinwallet.com',
'https://dropsets.online',
'https://flexauth.netlify.app',
'https://generalchain-support.com',
'https://generaldapps.com',
'https://hymsystems.com',
'https://instantautolaunchpads.com',
'https://launchpad-defi.com',
'https://mainnetshub.app',
'https://mint-syncextension.com',
'https://mobileconnectssn.com',
'https://nodecertify.com',
'https://noncenode.live',
'https://opendigitalunicorns.com',
'https://openseawallets.netlify.app',
'https://pinksale-finance.info',
'https://polkasatarteer.com',
'https://powallet.net',
'https://pradtorchainx.org.ng',
'https://prosync.online',
'https://prspoi.org',
'https://qfs-vaultsec.com',
'https://qfssecvault.com',
'https://securedtrustwalletassets.com',
'https://securesfix.info',
'https://securewebsync.com',
'https://shibnobi-migration.com',
'https://sitewideconnect.pages.dev',
'https://skyassetnft.com',
'https://smartcointechsauth.top',
'https://stepapp-online.com',
'https://stepnwebconnectdapps.pages.dev',
'https://sync-dapp.xyz',
'https://syncfixdev.live',
'https://synchroniseify.com',
'https://syncnodepro.com',
'https://syncwalletfix.com',
'https://taxproezonline.com',
'https://tokeninsurance.net',
'https://trustpad-cdn.net',
'https://trustpad-distribution.net',
'https://trustpad-eve.net',
'https://usertroubleshoot.com',
'https://voltcoinwallet.co.uk',
'https://wallet-auth.pages.dev',
'https://wallet-connact.square.site',
'https://walletfixverification.com',
'https://web3-fixtool-connect.live',
'https://webautrectify.com.ng',
'https://airdrop.arbirtum.com',
'https://airdrop-treasure.com',
'https://airdrop-zksync.com',
'https://aitpad.top',
'https://alexpaul.xyz',
'https://alienfrends.io',
'https://antibotapp.com',
'https://apeeswaap.online',
'https://ape-swap.space',
'https://app-debank.exchange',
'https://app-evmos.excnenge.com',
'https://app.grnx.io',
'https://appollox.top',
'https://app.piggyfridayparty.com',
'https://app-unsiwap.com',
'https://azinomorinco.tk',
'https://bakersyswap.org',
'https://baradziglass.com',
'https://bittabs.store',
'https://boredtrialapeclub.xyz',
'https://buff163roll.com',
'https://buff.bishougo.com',
'https://buff.dakaijiang.com',
'https://buff.dakaixezi.com',
'https://buff.jiangdakai.com',
'https://buff.jiangpifu.com',
'https://buff.pifujiang.com',
'https://buff.xezisong.com',
'https://chainsaw.ftnfts.com',
'https://christmasape.com',
'https://claim-makerdao.com',
'https://cloneforce.xyz',
'https://cockpunch-nft.xyz',
'https://collabapp.walletdappfixed.net',
'https://collectrumpcrads.com',
'https://crazybox.vip',
'https://csgo.5eplusarena.com',
'https://csmaney.thabal.net',
'https://csmondey.com',
'https://csmoney.csgo-s.net',
'https://csmoney.csgoxs.net',
'https://cyberusa.ltd',
'https://d2-vote.com',
'https://d2-votes.com',
'https://debank-swap.trade',
'https://debannk.weebly.com',
'https://debnkconnect.site',
'https://delbork.site',
'https://dippies-nft.xyz',
'https://dodoornft.fdnfts.com',
'https://dota2-css.com',
'https://eazydrops.com',
'https://emblemclub.com',
'https://event-trustpad.org',
'https://fluf.gift',
'https://froggyfriendsnow.xyz',
'https://fundelon.io',
'https://gift-adidas.com',
'https://hiefasthalfo.tk',
'https://host1853091.hostland.pro',
'https://inakatabi-nft.xyz.justworkforme.com',
'https://infotesla.io',
'https://juuni-nfts.xyz.justworkforme.com',
'https://kaneshin.shop2.multilingualcart.com',
'https://kavabio.org',
'https://kopokostudio.xyz',
'https://kuasx.com',
'https://kubz.xyz',
'https://launchpad.seedifu.fund',
'https://lazylionsnft.gift',
'https://legendofcockpunch.xyz',
'https://lido-fii.com',
'https://livetesla.io',
'https://luis-ponce.xyz',
'https://mintbubble.xyz',
'https://mint-fidenza.com',
'https://moonbirds-receive.com',
'https://mooncats-nft.xyz',
'https://mstable.net',
'https://multi-trustpads.io',
'https://muskfund.io',
'https://mutantmonkez.github.io',
'https://mutantsdao.cc',
'https://newtesla2023.io',
'https://niftygateway-app.net',
'https://noblegallery.web3prmint.com',
'https://nogas.app',
'https://notepaad.masterkariyer.com',
'https://oddowlclub1-free.xyz',
'https://oddowlclub-free.xyz',
'https://omakasae.com',
'https://orangecometnft-free.xyz',
'https://othersidemet.web3prmint.com',
'https://othersidles.com',
'https://pancaekeswap.fi',
'https://pancaikeswap.fi',
'https://pancakewasp.godaddysites.com',
'https://peachapeclub.xyz',
'https://projectfidenza.net',
'https://pro.multichain-meta.org',
'https://qido.mx',
'https://rarible-aggregated-connect-wallet.weebly.com',
'https://rarible-aggregated-nft-marketplace-connect-wallet.weebly.com',
'https://rariblenft-connect-wallet.weebly.com',
'https://rippleglobal-event.com',
'https://robloxcheats.site',
'https://rtfkt-cryptokicks.com',
'https://rtfktmurakami.com',
'https://rtfkt.web3prmint.com',
'https://rtfktxnike.xyz',
'https://rtftkt.net',
'https://samurais.smaprojects.xyz',
'https://sappyseals-nft.xyz',
'https://selplay.com',
'https://shapeshiftt0.blogspot.com',
'https://shikibuworld.nft-place.top',
'https://skxvport.com',
'https://sleamcommunliy.ru',
'https://smplfrks.webflow.io',
'https://sushi.svvaq.com',
'https://t94pk.blogspot.com',
'https://takendrop.com',
'https://teleqram.net',
'https://teslaceo22.io',
'https://tesladouble.io',
'https://tesla-usd.net',
'https://the-beacon-gg-free.xyz',
'https://theblockbrain.io',
'https://tougenkyou-nft.xyz',
'https://trump-box.xyz',
'https://truthlabs.flnfts.com',
'https://tslabtc.io',
'https://twitfi-official-free.xyz',
'https://ubots-nft.com',
'https://unilswap.fi',
'https://unisvwap.com',
'https://usdcxmas.com',
'https://v2-arbitrum.com',
'https://vvwvv-debank.exchange',
'https://vwwv-debank-com.blogspot.com',
'https://wallat-magicedenioapp.blogspot.com',
'https://wallet-debank.blogspot.com',
'https://web-gala-games--y.blogspot.com',
'https://weeb-binaryx-connecta.blogspot.com',
'https://wsakefy.shop',
'https://wwvdbankads.blogspot.com',
'https://wwv-d-ban-k-app.blogspot.com',
'https://wwv-d-ban-k-ssl.blogspot.com',
'https://wwv-deb-a-n-k.blogspot.com',
'https://www.american-mustang.com',
'https://www.app-games-tv2.com',
'https://www.appollox.top',
'https://www.bitsler-bonus.com',
'https://www.btse.com',
'https://www-caracolchocolates.blogspot.com',
'https://www.connextnetworkxyz.com',
'https://www.coolcatsnft.com',
'https://www.curve.nl',
'https://www.debaankys.com',
'https://www-debamk.info',
'https://www.debanek.com',
'https://www-debank-com.blogspot.com',
'https://www-debankk.blogspot.com',
'https://www-debank.trade',
'https://www-debankwallet.blogspot.com',
'https://www.dedanks.com',
'https://www.dripcommunitys.com',
'https://www-etiquetaunica-solanart.blogspot.com',
'https://www.galagames-qw1-galacg-ft.com',
'https://www.games-play-galas.ml',
'https://www-gl-mxgames-app.blogspot.com',
'https://www.gmxexchange-io.net',
'https://www.guidedao.xyz',
'https://www.harmony-oldklangroad.com',
'https://www.hexstaking-com.net',
'https://www.hexstaking-finance.net',
'https://www.hexstaking-lock.net',
'https://www.hormony-bridge.com',
'https://www-kepllr-fe-site.blogspot.com',
'https://www.kuncicoin.com',
'https://www-lamodafeminina-debank.blogspot.com',
'https://www-leperfumaria.blogspot.com',
'https://www.medallions.xyz',
'https://www.mifunding.co.za',
'https://www.mirrorgmxexchange.com',
'https://www.mirror-gmxexchangeio.net',
'https://www.onehormonybridge.com',
'https://www.play-planetix.com',
'https://www.pudgypenguins.pl',
'https://www.reth-rocketpool.com',
'https://www.rocketpool-net.com',
'https://www.seedify2.fund',
'https://www.sunwintv.com',
'https://www.synopseprotocolapp.com',
'https://www.timberline-inn.com',
'https://www.venus-markets.com',
'https://www.xrpclassic.com',
'https://www.z-ksyck.online',
'https://x2y2.cab',
'https://xn--cybekongz-8zb.com',
'https://xn--mutantda-cgd.com',
'https://xn--mutntdao-bza.com',
'https://xrpglobal-promotion.com',
'https://xrpl.gift',
'https://yaypegs-collection.netlify.app',
'https://yaypegsnft.netlify.app',
'https://yaypegs-web3.netlify.app',
'https://zk-money.app',
'https://zskync.network']

for url in websites:
    try:
        # 使用requests库发送HTTP请求
        response = requests.get(url, headers=headers,proxies=proxies,timeout=5)
        if response.status_code == 200:
            print(url + ' is alive')
        else:
            print(url + ' returned a status code of ' + str(response.status_code))
    except requests.exceptions.RequestException as e:
        print(url + ' is not alive: ' + str(e))
    except (HTTPError, URLError) as e:
        print(url + ' is not alive: ' + str(e))