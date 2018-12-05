<template>
  <div class="detail">
    <el-row
      :gutter="width > 1080 ? 10 : 0"
      type="flex">
      <el-col :span="width > 1080 ? 18 : 24">
        <el-card class="box-card">
          <div
            slot="header"
            class="head">
            <el-breadcrumb separator=">">
              <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
              <el-breadcrumb-item><a href="/">前端</a></el-breadcrumb-item>
              <el-breadcrumb-item>详情</el-breadcrumb-item>
            </el-breadcrumb>
          </div>
          <div class="content">
            <h2 class="title">
              {{ title }}
            </h2>
            <div class="author">
              <span>{{ author }} - {{ updatetime }}</span>
            </div>
            <div
              class="article"
              v-html="content"></div>
          </div>
        </el-card>
      </el-col>
      <el-col
        v-if="width > 1080"
        :span="6">
        <el-card class="box-card">
          <div
            slot="header"
            class="clearfix">
            <span>推荐</span>
            <el-button
              style="float: right; padding: 3px 0"
              type="text">更多</el-button>
          </div>
          <div
            v-for="o in 10"
            :key="o"
            class="text item">
            {{ '列表内容 ' + o }}
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  // import AsideCard from '~/components/AsideCard'
  export default {
    components: {
      // AsideCard
    },
    data () {
      return {
        width: '',
        title: '瑞幸咖啡、连咖啡、星巴克必有一战',
        author: '李小白',
        updatetime: '6天前',
        content: `<div class="articleDetail" deep="5">
                        <p>在美国，人均每年要喝掉400杯咖啡；在日本、韩国，人均每年要喝掉200杯咖啡；而在中国，这个数字是5~6杯。如果只算国内一线城市，人均每年的咖啡消费数也只有20杯。</p><p>中国与发达国家在咖啡消费数量上的差距，从侧面也反应了咖啡市场在国内有非常广阔的发展空间，相关评估机构的数据是至少有近千亿的市场。</p><p>所以，当你一次次地在朋友圈、办公室、商场看到 “Luckin coffee”和“连咖啡”们的时候，请不要惊讶。这只是咖啡市场争夺战的序幕。</p><p>“唤醒世界的香味”正逐渐唤醒国人</p><p>咖啡作为“世界饮料”，已经成为很多国家日常生活中不可或缺的存在。无论晨间还是午后，或者深夜加班，都离不开咖啡的陪伴。</p><p>国人喝到第一杯咖啡，历史可以追溯到“五口通商”时期，近代咖啡的流行主要依靠连锁品牌的带动。从最开始的“台系”上岛咖啡，到“美系”星巴克，再到“韩系”漫咖啡，经过二十多年的发展，形成了以星巴克为首的“一超多强”局面。</p><p><br data-filtered="filtered"></p><p><img alt="突破鄙视链，互联网咖啡欲打破星巴克的半壁江山" src="http://www.duoguyu.com/uploads/201805/23/201805231112195151.jpg"></p><p><br data-filtered="filtered"></p><p>星巴克在中国市场，用了17年的时间，从一线城市开始逐渐渗透到大部分三四线城市，截至2017年底，星巴克在中国大陆门店数量已经超过3000家。而在五年内，星巴克要把这个数字提升到5000。</p><p>随着门店的发展，如今在很多商圈和写字楼都能轻易找到一家星巴克，曾经象征着品质和小资的星巴克咖啡逐渐变成了大众的日常消费品。</p><p>“咖啡鄙视链”高处不胜寒</p><p>目前国内线下咖啡市场，主要分为两大阵营：连锁品牌门店、精品咖啡门店。连锁品牌大家相对熟知，而精品咖啡门店主要面对的受众是有一定咖啡知识积累和口味辨别能力的进阶者，以更高的品质、独特的口味，还有冲调手法作为卖点，往往门店数量较少，一个城市可能只有一家，比如国外的Blue Bottle、% ARABICA，国内的质馆等。</p><p><br data-filtered="filtered"></p><p><img alt="突破鄙视链，互联网咖啡欲打破星巴克的半壁江山" src="http://www.duoguyu.com/uploads/201805/23/201805231112198941.jpg"></p><p><br data-filtered="filtered"></p><p>如果深入咖啡圈子里，会发现同样存在几条公认的鄙视链。</p><p><span class="text-remarks" style="box-sizing: border-box; color: rgb(153, 153, 153); line-height: 30px;">鄙视链A：精品咖啡馆＞星巴克/Costa＞上岛＞便利店咖啡＞快餐店咖啡＞速溶咖啡</span></p><p><span class="text-remarks" style="box-sizing: border-box; color: rgb(153, 153, 153); line-height: 30px;">鄙视链B：阿拉比卡豆＞罗伯斯塔豆</span></p><p><span class="text-remarks" style="box-sizing: border-box; color: rgb(153, 153, 153); line-height: 30px;">鄙视链C：手冲＞意式＞美式＞花式</span></p><p><span class="text-remarks" style="box-sizing: border-box; color: rgb(153, 153, 153); line-height: 30px;"><br data-filtered="filtered"></span></p><p>而从销量的角度来看，反而是处于鄙视链底端的品类销量最好，受众最广。深厚的群众基础，也是下一步咖啡市场消费升级的主力军。</p><p>鄙视链或许是比较稳固，但鄙视链上的人是需要有流动性的，否则，用什么来支撑一杯气质非凡的单品手冲的价格呢？</p><p>虽然精品咖啡馆处在鄙视链顶端，但从调查数据来看，保持长期的稳定客流并非易事。网红红一时，等流量和热度下来了，能让受众记住的，如果只是那一缕若隐若现的香味，那么经营状况恐怕不容乐观。</p><p>所以，有远见的经营者已经开始打造自己的精品咖啡品牌，并谨慎地开始了门店的扩张。以应对市场的下一步挑战。</p><p>互联网咖啡入局 欲打破星巴克的“半壁江山”</p><p>调查数据显示，在2017年中国连锁咖啡饮料品牌市场份额排行榜中，星巴克的市场份额达到51%，占据整个市场的半壁江山，上岛、Costa、麦咖啡紧随其后。</p><p>从连咖啡（Coffee Box）到瑞幸咖啡（luckin coffee），两大互联网咖啡品牌迅速走红，运用互联网思维和O2O打法，从外卖切入，打击星巴克最薄弱的一环，成为了办公室咖啡的新潮流。</p><p><br data-filtered="filtered"></p><p><img alt="突破鄙视链，互联网咖啡欲打破星巴克的半壁江山" src="http://www.duoguyu.com/uploads/201805/23/201805231112198392.jpg"></p><p><br data-filtered="filtered"></p><p>连咖啡诞生于2012年，以微信公众号为入口，早期通过提供星巴克、Costa等第三方品牌咖啡外送服务积累用户，从2015年8月开始转型做自有品牌的咖啡。在转型后，连咖啡受到了资本市场的青睐，2016年4月7日，连咖啡宣布完成B轮融资5000万元人民币，由华策影视领投。 2018年3月12日完成1.58亿元B+轮融资，由启明创投领投，高榕资本跟投。</p><p>而瑞幸咖啡瞄准了高品质新零售咖啡市场，号称目标是为消费者提供星巴克以外的第二个咖啡选择。瑞幸咖啡的天使轮融资来自神州优车董事长兼CEO陆正耀及瑞幸咖啡创始团队成员，有消息称，目前已有投资人沟通投资事宜，A轮融资将于4月份启动。</p><p>连咖啡，一家出色的互联网营销公司</p><p>连咖啡从本质来看，更像是一家互联网营销公司。从创立最初，连咖啡就选择了一条很轻的路。没有APP，一切功能、交易、营销都基于连咖啡的微信公众号，以及后来的连咖啡小程序。没有门店，只有配送站点，销售全靠外卖。</p><p>轻资产策略给连咖啡的发展带来了更多的可能性，连咖啡创始人王江（业内称为“连长”）也把更多的资金和精力放在了他更擅长的营销上。2016年年底，连咖啡打造出“咖啡库”的产品概念，把提前购买的咖啡存在虚拟的咖啡库中，在期限内可以自己下单享用，也可以赠送给微信好友。同时通过抢“咖啡福袋”，能累积“0.01~0.1杯”咖啡叠加到咖啡库中，积满1杯虚拟咖啡便可兑换成等量咖啡实物。这种玩法显然还要比外卖红包更吸引人。</p><p>2017年双11当天连咖啡单日销量突破30万，双12返场活动单日销量突破40万。除了低价折扣这种传统的促销活动外，连咖啡深谙社交营销关键点，是在情感上抓住用户，从而强化品牌记忆度。比如在去年七夕期间推出的“微苦邮局，情书乱递”活动，便受到众多用户的好评，并产生二次传播，通过裂变得到更低的流量和获客成本。</p><p><br data-filtered="filtered"></p><p><img alt="突破鄙视链，互联网咖啡欲打破星巴克的半壁江山" src="http://www.duoguyu.com/uploads/201805/23/201805231112199704.jpg"></p><p><br data-filtered="filtered"></p><p>背靠微信生态，给连咖啡带来了高速裂变式的用户增长。但在产品和服务上，连咖啡也有硬伤。从连咖啡的产品矩阵来看，有独特的明星产品“防弹咖啡”，此外是热咖啡、冰咖啡、雪昔、椰子水，整个矩阵有点有面，比较完整。</p><p>但从连咖啡所有的产品介绍和宣传来看，并未强调任何关于原材料、品质、制作水准方面的描述，重点放在了外卖的便捷、产品的包装上。事实上，连咖啡在出品水准上，也仅仅是接近麦咖啡、肯德基现磨的快餐店咖啡，品质上和星巴克还有一定距离。</p><p>此外，配送服务是连咖啡另一个潜在的危机，包括配送范围覆盖不足、配送时效性差、洒漏情况频发等等。一个简单的例子，上海浦东新区张江高科区域，是上海高科技企业聚集地，在附近上班的人，从人群匹配度上完美契合连咖啡目标用户。但非常诡异的是，以中环为界，连咖啡的配送服务只限于中环内，中环外不在服务范围，实际上中环边上至少有10幢写字楼，潜在用户可能有数万人。</p><p>商业机会往往转瞬即逝，特别是在尚未建立起产品壁垒、形成品牌区隔的阶段。上述未被覆盖的区域，在上个月，已经被直接竞争对手瑞幸咖啡拿下。面对瑞幸咖啡的强势挑战，连咖啡坚守的策略已略显保守。在一线城市找“下沉用户”似乎并不是一个明智的玩法。</p><p>瑞幸咖啡，10亿人民币能否成功教育市场？</p><p>相对于连咖啡而言，瑞幸咖啡起步更晚，但互联网化程度更高。在2017年10月诞生之初，便标榜“咖啡+O2O+新零售”模式。瑞幸咖啡创始团队主要来自神州体系，创始人兼CEO钱治亚是前神州优车COO， CMO杨飞此前也是神州优车CMO。钱治亚曾公开表示，要用10亿人民币教育中国的咖啡市场。</p><p>资金实力雄厚，也让瑞幸咖啡的扩张显得更大刀阔斧。瑞幸咖啡目前已经成功入驻北京、上海、广州、深圳、天津、福州、武汉等13个主流城市，门店数量已经超过300家。预计5月份将达成全国500家门店的规模。瑞幸咖啡的线下门店主要有3种类型：旗舰店（ELITE），悠享店（RELAX）、快取店（PICKUP），这些门店均为直营门店。所有门店都支持外送业务，配送服务与顺丰达成深度合作，只要有门店的的地方，都会以门店为织网，覆盖周边1.5~2公里区域。</p><p><br data-filtered="filtered"></p><p><img alt="突破鄙视链，互联网咖啡欲打破星巴克的半壁江山" src="http://www.duoguyu.com/uploads/201805/23/201805231112192147.jpg"></p><p><br data-filtered="filtered"></p><p>瑞幸咖啡主打性价比与高品质咖啡，号称目标是为消费者提供星巴克以外的第二个咖啡选择，未来要在国内打败星巴克。在保证品质方面，瑞幸咖啡在用料、调制、配送都下足了工夫。选用来自埃塞俄比亚的上等阿拉比卡豆，邀请WBC冠军咖啡师调配，保证30分钟内送达，“慢必赔”。</p><p>在实际体验过程中，抛开特殊天气外，一般能够在20分钟左右接到顺丰小哥的投递，和连咖啡一样，同样容易出现洒漏的情况，但在售后客服跟进的态度和积极度上，要比连咖啡客服更胜一筹。至于口味方面，水准已经跟星巴克十分接近。</p><p>在营销层面，由于整个购买环节必须使用luckin coffee的APP，在一定程度上提高了获客的门槛，但从长远来看，能够使用的营销手段和玩法可以更丰富。无论是邀请注册送咖啡、还是现阶段主打的“买二送一、买五送五”，都很简单粗暴，通过社交传播，推动新客下单第一杯。配合两位明星代言人，汤唯和张震的影响力，更容易让新用户产生移情效果。</p><p><br data-filtered="filtered"></p><p><img alt="突破鄙视链，互联网咖啡欲打破星巴克的半壁江山" src="http://www.duoguyu.com/uploads/201805/23/2018052311121976.jpg"></p><p><br data-filtered="filtered"></p><p>先声夺人后，瑞幸咖啡主要面临的挑战有以下三个：</p><p>1. 融资情况。由于门店扩张的重资产模式，必须保证资金链的稳定。另外也会影响给用户的补贴，甚至会因为由此产生的连锁效应影响到教育市场这个目标能否达成。</p><p>2. 品质坚守。高品质和性价比是目前瑞幸咖啡的两个重拳，在快速扩张过程中，与第三方配送合作中，都很容易出现管控不到位的情况。产品品质才是一个品牌生存下去的根本。</p><p>3. 星巴克的反击。面对互联网咖啡的强力冲击，行业老大星巴克不会坐以待毙，有消息称星巴克可能在近期重启外送服务。面临与星巴克潜在的直接对抗，还在成长中的瑞幸咖啡将如何应战？</p><p>回到最开始的论题，第三次咖啡浪潮何时会全面席卷中国，大众对咖啡的接受度和依赖度到底有多高？毕竟，广阔的中国市场并不局限在一二线城市。</p>                        </div>`
      }
    },
    watch: {
      width () {
        this.width = window.innerWidth
      }
    },
    mounted() {
      let width = window.innerWidth
      this.width = width
    }
  }
</script>

<style lang="less">
  .detail {
    padding-top: 80px;
    max-width: 1280px;
    margin: 0 auto;
  }
  .head {
    padding: 4px 30px;
    font-size: 14px;
  }
  .title {
    text-align: center;
    line-height: 56px;
  }
  .author {
    text-align: center;
    line-height: 36px;
    margin-bottom: 40px;
  }
  .content {
    padding: 30px;
    .articleDetail {
      p {
        margin-bottom: 12px;
        line-height: 26px;
        text-indent: 2rem;
         img {
          display: block;
          margin: 0 auto;
          // width: 100%;
          max-width: 850px;
        }
      }
    }
  }
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

</style>

