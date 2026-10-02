# -*- coding: utf-8 -*-
"""Guides: Mental maths."""

CAT = "Mental maths"

GUIDES = [

# ---------------------------------------------------------------- 1
dict(
    slug="mental-strategies", cat=CAT, nav="Mental maths strategies", read=7,
    h1="Mental maths strategies worth teaching",
    card="Nine strategies that turn hard sums into easy ones, with when to reach for each.",
    years="Years 2\u20136",
    seo="Mental maths strategies \u2014 nine methods that actually work | Math It!",
    desc="Practical mental arithmetic strategies: partitioning, compensation, near doubles, bridging through ten, and more. When to use each one and how to practise them.",
    keywords="mental maths strategies, mental arithmetic, partitioning, compensation maths, near doubles, bridging through ten, KS2 mental maths, mental maths tricks",
    intro="""<p>Mental maths is not about being fast at the same method you would write down. It is
      about having a handful of strategies and choosing a good one \u2014 turning 199 + 56 into
      200 + 56 \u2212 1 rather than grinding through columns in your head.</p>
      <p>What follows are the nine strategies that cover the overwhelming majority of mental
      calculations children meet, and the signal that tells you which to use.</p>""",
    steps=[
        ("Partitioning",
         "<p>Split numbers by place value and handle each part. 46 + 37 becomes 40 + 30 = 70, then "
         "6 + 7 = 13, then 70 + 13 = 83. This is the default for addition.</p>"),
        ("Compensation",
         "<p>Round to something easy, then correct. 199 + 56 \u2192 200 + 56 = 256, then \u2212 1 = "
         "255. Use it whenever a number is just under or just over a multiple of 10 or 100.</p>"),
        ("Bridging through ten",
         "<p>Break a jump at the nearest ten. 8 + 7 \u2192 8 + 2 = 10, then + 5 = 15. This is the "
         "foundation strategy in Key Stage 1 and it never stops being useful.</p>"),
        ("Near doubles",
         "<p>If a double is known, adjust. 7 + 8 \u2192 double 7 = 14, + 1 = 15. 15 + 16 \u2192 "
         "double 15 = 30, + 1 = 31.</p>"),
        ("Doubling and halving for multiplication",
         "<p>Halve one factor and double the other. 16 \u00d7 25 \u2192 8 \u00d7 50 \u2192 4 \u00d7 100 "
         "= 400. Enormously effective when one factor is even and the other is awkward.</p>"),
        ("Multiply by partitioning",
         "<p>13 \u00d7 7 \u2192 (10 \u00d7 7) + (3 \u00d7 7) = 70 + 21 = 91. The grid method, done "
         "mentally.</p>"),
        ("Counting on for subtraction",
         "<p>When numbers are close, count up. 2,003 \u2212 1,987 \u2192 up 13 to 2,000, then 3 more = "
         "16. Far safer than exchanging across zeros in your head.</p>"),
        ("Use known facts to reach unknown ones",
         "<p>If 6 \u00d7 7 = 42 is secure, then 6 \u00d7 70 = 420, 60 \u00d7 7 = 420, 0.6 \u00d7 7 = 4.2 "
         "and 42 \u00f7 6 = 7 all follow without new learning.</p>"),
        ("Reorder to make it easy",
         "<p>Addition and multiplication can be rearranged. 17 + 36 + 3 \u2192 17 + 3 + 36 = 56. "
         "2 \u00d7 17 \u00d7 5 \u2192 2 \u00d7 5 \u00d7 17 = 170.</p>"),
    ],
    examples=[
        ("Work out 198 + 47 mentally.",
         ["198 is 2 below 200 \u2014 compensation is the signal.",
          "200 + 47 = 247.",
          "Take the 2 back off."],
         "245"),
        ("Work out 24 \u00d7 25 mentally.",
         ["25 is awkward, 24 is even \u2014 double and halve.",
          "12 \u00d7 50 = 600.",
          "Or halve again: 6 \u00d7 100."],
         "600"),
        ("Work out 5,002 \u2212 4,987 mentally.",
         ["The numbers are close, so count on.",
          "4,987 up to 5,000 is 13.",
          "5,000 up to 5,002 is 2."],
         "15"),
        ("Work out 7 \u00d7 48 mentally.",
         ["48 is 2 below 50 \u2014 compensation again.",
          "7 \u00d7 50 = 350.",
          "7 \u00d7 2 = 14, so subtract 14."],
         "336"),
    ],
    mistakes=[
        ("Doing the written column method in your head.",
         "Working right to left mentally forces you to hold carries. Mental methods go left to right: 46 + 37 starts with 40 + 30."),
        ("Compensating in the wrong direction.",
         "If you rounded <em>up</em> to make it easy, you must take the difference back <em>off</em>. Say it aloud: \u2018I added 2, so I take 2 away.\u2019"),
        ("Having one strategy and forcing everything through it.",
         "Partitioning 2,003 \u2212 1,987 is miserable; counting on takes three seconds. Picking the strategy is the skill."),
        ("Practising only with a pencil in hand.",
         "If the pencil is available it will get used. Do mental practice genuinely mentally, with answers said aloud or typed."),
    ],
    sections=[
        ("How to pick a strategy",
         """<p>The number itself usually tells you:</p>
         <ul>
           <li>Ends in 8 or 9, or just past a 10 or 100 \u2192 <strong>compensation</strong>.</li>
           <li>The two numbers are close together, in a subtraction \u2192 <strong>count on</strong>.</li>
           <li>One factor is even and the other is 5, 25 or 50 \u2192 <strong>double and halve</strong>.</li>
           <li>The two numbers differ by 1 or 2, in an addition \u2192 <strong>near doubles</strong>.</li>
           <li>Nothing special \u2192 <strong>partition</strong>.</li>
         </ul>
         <p>Spending a lesson just <em>classifying</em> calculations \u2014 without answering them \u2014
         is unexpectedly powerful.</p>"""),
        ("Why mental maths still matters",
         """<p>Partly because KS2 SATs include an arithmetic paper under time pressure, where
         mental shortcuts buy minutes for the harder questions. But mostly because mental
         calculation is where number sense lives. A child who knows that 24 \u00d7 25 is 600 because
         of doubling and halving understands multiplication in a way that one who only knows the
         column method does not.</p>
         <p>It is also the only arithmetic most adults actually use. Nobody sets out long
         multiplication at the supermarket.</p>"""),
        ("Building it into ordinary life",
         """<p>Car journeys and shopping are better practice than worksheets, because the numbers
         are real and the pressure is gentle. Ask for the total of two prices, the change from
         \u00a320, how many minutes until arrival, how much three of something costs. Keep it short
         and keep it light \u2014 two minutes of cheerful mental maths a day outperforms a
         twenty-minute battle.</p>"""),
    ],
    faqs=[
        ("Should children use fingers?",
         "In Key Stage 1, absolutely \u2014 fingers are a legitimate representation of number and the research supports them. The aim is to outgrow them naturally as recall builds, not to ban them."),
        ("How fast should mental recall be?",
         "For number bonds and tables, within about three seconds. Slower than that usually means the fact is being calculated rather than recalled, which is fine while learning but will not survive timed conditions."),
        ("Is there still a mental maths test in SATs?",
         "The separate mental arithmetic test was scrapped in 2016. Arithmetic Paper 1 is written, but it is tight on time, so mental strategies still matter a great deal."),
        ("My child gets the right answer by a strange route. Should I correct it?",
         "Not if it is reliable and reasonably quick. Unusual but valid strategies are a sign of genuine number sense. Only intervene if the method is slow or breaks on bigger numbers."),
    ],
    cta=("Practise mental arithmetic", "practice.html?year=5&level=medium"),
    related=["number-bonds", "times-tables", "column-addition", "rounding"],
),

# ---------------------------------------------------------------- 2
dict(
    slug="number-bonds", cat=CAT, nav="Number bonds", read=5,
    h1="Number bonds: the facts everything else rests on",
    card="Bonds to 10, 20, 100 and 1 \u2014 what to learn, in what order, and how to test them.",
    years="Years 1\u20134",
    seo="Number bonds explained \u2014 to 10, 20, 100 and 1 | Math It!",
    desc="What number bonds are, which ones children need to know by heart, how bonds to 10 generate bonds to 100 and to 1, and quick ways to test and practise them.",
    keywords="number bonds, number bonds to 10, number bonds to 20, number bonds to 100, bonds to 1 decimals, KS1 number bonds, year 2 number bonds",
    intro="""<p>A number bond is a pair that adds to a given total. The bonds to 10 are
      0+10, 1+9, 2+8, 3+7, 4+6, 5+5 and their reverses \u2014 eleven facts in total, and arguably the
      most valuable eleven facts in primary maths.</p>
      <p>Almost every mental strategy depends on them. Bridging through ten, counting on, column
      addition, finding change, converting decimals \u2014 all of it runs faster when bonds are
      automatic.</p>""",
    steps=[
        ("Learn the bonds to 10 to automaticity",
         "<p>Not \u201ccan work them out\u201d \u2014 instant. Asked for the partner of 7, a child "
         "should say 3 without a pause. There are only six distinct pairs.</p>"),
        ("Extend to 20",
         "<p>Two routes. Bonds within 20 that bridge ten (13 + 7) and the doubles-based ones "
         "(9 + 11). Children who know bonds to 10 pick these up quickly.</p>"),
        ("Scale up to 100 in tens",
         "<p>30 + 70 = 100 is just 3 + 7 = 10 with everything ten times bigger. Say it that way "
         "explicitly and the whole set arrives at once.</p>"),
        ("Then bonds to 100 in ones",
         "<p>37 + 63 = 100. The method: make the tens add to 90 and the ones add to 10. "
         "30 + 60 = 90, 7 + 3 = 10. This is exactly how shop change is calculated.</p>"),
        ("Finally bonds to 1 with decimals",
         "<p>0.3 + 0.7 = 1 and 0.37 + 0.63 = 1. Same facts again, shifted. If bonds to 100 are "
         "secure these take about ten minutes to learn.</p>"),
    ],
    examples=[
        ("What is the bond partner of 6 to make 10?",
         ["6 + ? = 10.", "Count on from 6: 7, 8, 9, 10 \u2014 four steps."],
         "4"),
        ("What must be added to 37 to make 100?",
         ["Tens must reach 90: 30 + 60.",
          "Ones must reach 10: 7 + 3.",
          "So the partner is 60 + 3."],
         "63"),
        ("You pay with \u00a320 for something costing \u00a313.45. What change?",
         ["Pence to the next pound: 45p + 55p = \u00a31.",
          "\u00a314 up to \u00a320 is \u00a36.",
          "Total change \u00a36 + 55p."],
         "\u00a36.55"),
        ("What is 0.42 + ? = 1?",
         ["Bonds to 100: 42 + 58 = 100.",
          "Shift both to hundredths."],
         "0.58"),
    ],
    mistakes=[
        ("Counting on fingers every time, well into Year 4.",
         "Fingers are fine while learning, but bonds to 10 should be recalled. If they are still being counted in Year 4, go back and drill the six pairs directly."),
        ("Knowing 7 + 3 but not 3 + 7.",
         "Addition is commutative. Always rehearse pairs both ways round, and include the subtraction: 10 \u2212 3 = 7."),
        ("Treating bonds to 100 as a brand new set to memorise.",
         "They are bonds to 10 scaled up, plus one adjustment for the ones column. Teach the link, not 50 new facts."),
        ("Practising bonds in order, 0+10, 1+9, 2+8\u2026",
         "That builds sequence memory. Shuffle them, and ask for the partner rather than the total."),
    ],
    sections=[
        ("Why bonds beat counting",
         """<p>A child who computes 8 + 5 by counting on five has to hold the running total while
         tracking how many steps remain \u2014 two things at once. A child who knows bonds does
         8 + 2 = 10, then 10 + 3 = 13: two instant recalls and no tracking.</p>
         <p>The difference matters most when the sum is part of something bigger. In a long
         multiplication, every column addition that has to be counted out is working memory stolen
         from the actual problem.</p>"""),
        ("Testing them properly",
         """<p>Three quick formats, about a minute each:</p>
         <ul>
           <li><strong>Partner game.</strong> You say a number, they say its partner to 10. Then to
           100. Then to 1.</li>
           <li><strong>Missing number.</strong> Write 6 + ? = 10 and ? + 40 = 100.</li>
           <li><strong>Change.</strong> \u201cIt costs \u00a32.70 and I pay with a fiver.\u201d</li>
         </ul>
         <p>If any of those takes longer than three seconds, the bond is being calculated rather
         than recalled.</p>"""),
        ("What comes next",
         """<p>Once bonds are automatic, the natural next steps are the
         <a href="times-tables.html" class="link">times tables</a> and the
         <a href="mental-strategies.html" class="link">mental strategies</a> that build on both. By
         the end of Year 4 a child with secure bonds and secure tables has the entire factual base
         the rest of primary maths assumes.</p>"""),
    ],
    faqs=[
        ("What age should number bonds to 10 be known?",
         "End of Year 1 in England for bonds to 10, and bonds to 20 by the end of Year 2. Bonds to 100 follow in Year 2 to 3."),
        ("What is the difference between number bonds and number facts?",
         "Number bonds specifically means pairs that make a given total. \u2018Number facts\u2019 is the wider category, including tables and doubles."),
        ("Are number bonds the same as part-whole models?",
         "A part-whole model is the diagram often used to teach them \u2014 a whole at the top with two parts beneath. The bond is the fact; the model is the picture."),
        ("How do bonds help with subtraction?",
         "Every bond is two subtractions. 7 + 3 = 10 also tells you 10 \u2212 3 = 7 and 10 \u2212 7 = 3. Teaching all three together halves the work."),
    ],
    cta=("Practise number bonds", "practice.html?year=3&level=easy"),
    related=["mental-strategies", "times-tables", "column-addition", "place-value"],
),

]
