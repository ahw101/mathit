# -*- coding: utf-8 -*-
"""Guides: Ratio, algebra and measures."""

CAT = "Ratio, algebra & measures"

GUIDES = [

# ---------------------------------------------------------------- 1
dict(
    slug="ratio-and-proportion", cat=CAT, nav="Ratio and proportion", read=6,
    h1="Ratio and proportion",
    card="Share an amount in a given ratio, scale a recipe, and tell ratio from fraction.",
    years="Year 6",
    seo="Ratio and proportion explained \u2014 sharing, scaling and simplifying | Math It!",
    desc="How to simplify a ratio, share an amount in a given ratio using the parts method, scale recipes, and avoid confusing ratio with fraction.",
    keywords="ratio and proportion, sharing in a ratio, simplifying ratios, ratio problems, scaling recipes, year 6 ratio, KS2 ratio",
    intro="""<p>A ratio compares two or more quantities. 3:2 means that for every 3 of the first thing
      there are 2 of the second. Proportion is the related idea of quantities changing together at a
      fixed rate \u2014 double the recipe, double every ingredient.</p>
      <p>One distinction is worth nailing down before anything else: a ratio compares part to part,
      while a fraction compares part to whole. Confusing those two causes most ratio errors.</p>""",
    steps=[
        ("Count the total parts",
         "<p>In the ratio 3:2 there are 3 + 2 = 5 parts altogether. This is the number you divide "
         "by, and finding it is always step one.</p>"),
        ("Find the value of one part",
         "<p>Divide the total amount by the number of parts. \u00a340 shared in 3:2 gives "
         "40 \u00f7 5 = \u00a38 per part.</p>"),
        ("Multiply out each share",
         "<p>3 \u00d7 8 = \u00a324 and 2 \u00d7 8 = \u00a316.</p>"),
        ("Check the shares add back to the total",
         "<p>24 + 16 = 40. If they do not, something has gone wrong \u2014 and this check catches "
         "it immediately.</p>"),
        ("Simplify ratios the way you simplify fractions",
         "<p>Divide every part by the same number. 12:18 \u2192 \u00f7 6 \u2192 2:3. A ratio is in "
         "its simplest form when no whole number above 1 divides all the parts.</p>"),
        ("Scale by multiplying every part equally",
         "<p>To make 1.5 times a recipe written for 4, multiply every ingredient by 1.5. The ratio "
         "between the ingredients must stay identical.</p>"),
    ],
    examples=[
        ("Share \u00a360 between two people in the ratio 7:5.",
         ["Total parts: 7 + 5 = 12.",
          "One part: 60 \u00f7 12 = 5.",
          "Shares: 7 \u00d7 5 = 35 and 5 \u00d7 5 = 25.",
          "Check: 35 + 25 = 60."],
         "\u00a335 and \u00a325"),
        ("Simplify the ratio 18:24:30.",
         ["Find the highest common factor of 18, 24 and 30.",
          "All three divide by 6.",
          "18 \u00f7 6 = 3, 24 \u00f7 6 = 4, 30 \u00f7 6 = 5."],
         "3:4:5"),
        ("A recipe for 4 people needs 300 g of flour. How much for 10?",
         ["Find the amount for 1 person: 300 \u00f7 4 = 75 g.",
          "Multiply for 10 people: 75 \u00d7 10."],
         "750 g"),
        ("Paint is mixed 2 parts blue to 3 parts yellow. What fraction is yellow?",
         ["Total parts: 2 + 3 = 5.",
          "Yellow is 3 of those 5 parts.",
          "The ratio 2:3 gives the fraction 3/5, not 3/2."],
         "3/5"),
    ],
    mistakes=[
        ("Treating the ratio 3:2 as the fraction 3/2 of the total.",
         "Ratio compares part to part. As fractions of the whole, 3:2 means 3/5 and 2/5."),
        ("Dividing the total by one side of the ratio instead of by the total parts.",
         "\u00a340 shared in 3:2 means dividing by 5, never by 3 or by 2."),
        ("Simplifying only some parts of a ratio.",
         "Every part must be divided by the same number, or the comparison itself changes."),
        ("Adding the same amount to each part to scale up.",
         "Scaling multiplies. Doubling a recipe multiplies every ingredient by 2 \u2014 adding 100 g to each would wreck the proportions."),
    ],
    sections=[
        ("Ratio and fraction side by side",
         """<p>A bag holds 3 red counters and 2 blue ones.</p>
         <ul>
           <li><strong>Ratio</strong> of red to blue: 3:2 \u2014 part compared to part.</li>
           <li><strong>Fraction</strong> that is red: 3/5 \u2014 part compared to whole.</li>
           <li><strong>Percentage</strong> red: 60%.</li>
         </ul>
         <p>Three correct descriptions of one bag. Asking a child to produce all three for the same
         situation is the fastest way to secure the distinction for good.</p>"""),
        ("The difference-between question type",
         """<p>\u201cTwo people share money in the ratio 7:5. One gets \u00a320 more than the other.
         How much was shared altogether?\u201d</p>
         <p>The difference is 7 \u2212 5 = 2 parts, and that equals \u00a320. So one part is
         \u00a310, and the total is 12 parts = \u00a3120.</p>
         <p>Children who have only practised \u201cshare this total\u201d freeze here. The fix is to
         ask the same opening question in every ratio problem: <em>what is one part worth?</em></p>"""),
        ("Scaling, maps and recipes",
         """<p>Proportion underlies map scales, model making and enlargements. A scale of 1:50,000
         means 1 cm on the map represents 50,000 cm \u2014 that is 500 m \u2014 in real life.</p>
         <p>It also underlies currency conversion, speed, density and recipe conversion, which is
         why ratio is one of the highest-value topics in Year 6. It reappears constantly throughout
         secondary school.</p>"""),
    ],
    faqs=[
        ("What is the difference between ratio and proportion?",
         "A ratio compares quantities (3:2). A proportion states that two ratios are equal, which is what lets you scale \u2014 3:2 is the same proportion as 6:4."),
        ("How do I write a ratio as a fraction?",
         "Add the parts to get the whole. In 3:2 the first quantity is 3/5 of the total and the second is 2/5."),
        ("Does the order of a ratio matter?",
         "Very much. 3:2 red to blue is not the same as 2:3 red to blue. Always write down which quantity is named first."),
        ("Can a ratio have more than two parts?",
         "Yes. 2:3:5 shares something three ways, with 10 parts in total. The method is unchanged \u2014 find one part, then multiply out."),
    ],
    cta=("Practise ratio problems", "practice.html?year=6&level=hard"),
    related=["fractions-of-amounts", "percentages-of-amounts", "simple-algebra", "equivalent-fractions"],
),

# ---------------------------------------------------------------- 2
dict(
    slug="simple-algebra", cat=CAT, nav="Simple algebra", read=6,
    h1="Simple algebra: letters standing for numbers",
    card="Formulae, missing numbers and one-step equations, without the mystique.",
    years="Year 6",
    seo="Simple algebra for primary \u2014 formulae and missing numbers | Math It!",
    desc="Primary algebra explained: using letters for unknowns, substituting into formulae, solving one-step and two-step equations, and expressing missing-number problems algebraically.",
    keywords="simple algebra, KS2 algebra, year 6 algebra, substituting into formulae, solving equations, missing number problems, algebra for primary",
    intro="""<p>Algebra is arithmetic with a letter standing in for a number you do not know yet.
      That is genuinely all it is. 7 + ? = 12 and 7 + <em>n</em> = 12 are the same question; the
      second simply uses a letter instead of a box.</p>
      <p>Year 6 is where letters are introduced formally, and children who have been answering
      missing-number questions since Year 2 are already most of the way there.</p>""",
    steps=[
        ("A letter is just an unknown number",
         "<p><em>n</em>, <em>x</em>, <em>a</em> \u2014 the choice of letter means nothing at all. It "
         "is a placeholder for one particular number.</p>"),
        ("Drop the multiplication sign",
         "<p>3<em>n</em> means 3 \u00d7 <em>n</em>, and <em>ab</em> means <em>a</em> \u00d7 "
         "<em>b</em>. The \u00d7 is left out because it looks too much like the letter x.</p>"),
        ("Substitute by replacing the letter",
         "<p>If <em>n</em> = 4, then 3<em>n</em> + 2 becomes 3 \u00d7 4 + 2 = 14. Write the "
         "substitution out in full before calculating anything.</p>"),
        ("Solve by doing the inverse to both sides",
         "<p><em>n</em> + 7 = 12 \u2192 subtract 7 from both sides \u2192 <em>n</em> = 5. "
         "5<em>n</em> = 40 \u2192 divide both sides by 5 \u2192 <em>n</em> = 8.</p>"),
        ("Undo in reverse order for two steps",
         "<p>3<em>n</em> + 2 = 17. Undo the + 2 first: 3<em>n</em> = 15. Then undo the \u00d7 3: "
         "<em>n</em> = 5. You peel the operations off in the opposite order to BIDMAS.</p>"),
        ("Always check by substituting back",
         "<p>Put <em>n</em> = 5 into 3<em>n</em> + 2: 15 + 2 = 17. Correct.</p>"),
    ],
    examples=[
        ("If a = 7, work out 4a \u2212 3.",
         ["4a means 4 \u00d7 a.",
          "4 \u00d7 7 = 28.",
          "28 \u2212 3."],
         "25"),
        ("Solve n + 14 = 31.",
         ["The inverse of adding 14 is subtracting 14.",
          "Do it to both sides: n = 31 \u2212 14."],
         "n = 17"),
        ("Solve 6n = 54.",
         ["6n means 6 \u00d7 n.",
          "The inverse of multiplying by 6 is dividing by 6.",
          "n = 54 \u00f7 6."],
         "n = 9"),
        ("Solve 2n + 5 = 19.",
         ["Undo the + 5 first: 2n = 14.",
          "Then undo the \u00d7 2: n = 7.",
          "Check: 2 \u00d7 7 + 5 = 19."],
         "n = 7"),
        ("The perimeter of a rectangle is P = 2(l + w). Find P when l = 9 and w = 4.",
         ["Substitute: P = 2 \u00d7 (9 + 4).",
          "Brackets first: 9 + 4 = 13.",
          "2 \u00d7 13."],
         "P = 26"),
    ],
    mistakes=[
        ("Reading 3n as \u2018thirty-something\u2019, or as 3 + n.",
         "3n is 3 \u00d7 n. Say \u2018three lots of n\u2019 out loud until it is automatic."),
        ("Doing something to one side of the equation only.",
         "An equation is a balance. Whatever you do to the left you must also do to the right, or it stops being true."),
        ("Undoing the operations in BIDMAS order.",
         "To solve, you reverse BIDMAS: deal with addition and subtraction first, multiplication and division second."),
        ("Assuming different letters must stand for different numbers.",
         "They can be equal. In a + b = 10, both a and b could be 5."),
    ],
    sections=[
        ("What Year 6 actually covers",
         """<p>The National Curriculum asks Year 6 children to use simple formulae, generate and
         describe linear number sequences, express missing-number problems algebraically, find
         pairs of numbers that satisfy an equation with two unknowns, and enumerate possibilities
         of combinations of two variables.</p>
         <p>Note what is <em>not</em> there: expanding brackets, collecting like terms, simultaneous
         equations, or anything involving <em>x</em>\u00b2. All of that is Key Stage 3.</p>"""),
        ("Equations with two unknowns",
         """<p>\u201cFind all the pairs of whole numbers where a + b = 10.\u201d The answer is a list,
         not a single value: (0, 10), (1, 9), (2, 8) and so on up to (10, 0).</p>
         <p>This is a Year 6 favourite because it shows that an equation with two unknowns usually
         has many solutions. Work systematically \u2014 start at 0 and count up \u2014 so that none
         are missed and none are repeated.</p>"""),
        ("Formulae children already know",
         """<p>Algebra is less alien than it looks, because the formulae are familiar:</p>
         <ul>
           <li>Area of a rectangle: A = l \u00d7 w</li>
           <li>Perimeter of a rectangle: P = 2(l + w)</li>
           <li>Area of a triangle: A = (b \u00d7 h) \u00f7 2</li>
           <li>Cost: total = price \u00d7 quantity</li>
         </ul>
         <p>Substituting numbers into these is exactly the skill being assessed, and children have
         been doing it since Year 4 without anyone calling it algebra.</p>"""),
    ],
    faqs=[
        ("Why do we use letters instead of numbers?",
         "To describe a relationship that holds for every number, not just one. A = l \u00d7 w is true for all rectangles, which no single arithmetic statement could capture."),
        ("What does 3n mean?",
         "3 \u00d7 n. The multiplication sign is omitted because it is easily confused with the letter x."),
        ("Is algebra really on the KS2 curriculum?",
         "Yes, since 2014. Year 6 covers simple formulae, linear sequences, missing-number problems expressed algebraically, and equations with two unknowns."),
        ("How do I check an algebra answer?",
         "Substitute your value back into the original equation. If both sides come out equal, the answer is right."),
    ],
    cta=("Practise simple algebra", "practice.html?year=6&level=hard"),
    related=["number-sequences", "order-of-operations", "ratio-and-proportion", "metric-units"],
),

# ---------------------------------------------------------------- 3
dict(
    slug="number-sequences", cat=CAT, nav="Number sequences", read=5,
    h1="Number sequences and finding the rule",
    card="Spot the pattern, state the rule, and continue a sequence in either direction.",
    years="Years 4\u20136",
    seo="Number sequences explained \u2014 how to find the rule | Math It!",
    desc="How to find the rule of a number sequence, continue it forwards and backwards, recognise linear sequences, and spot squares, triangular numbers and Fibonacci.",
    keywords="number sequences, finding the rule, linear sequences, nth term primary, continuing sequences, triangular numbers, year 6 sequences, KS2 patterns",
    intro="""<p>A sequence is a list of numbers that follows a rule. Finding that rule is the whole
      task, and once you have it you can continue the sequence in either direction or jump ahead to
      any term you like.</p>
      <p>Most primary sequences are <strong>linear</strong>: the same amount is added or subtracted
      each time. A few multiply instead, and a handful are famous patterns worth recognising on
      sight.</p>""",
    steps=[
        ("Find the gaps between consecutive terms",
         "<p>Write the differences underneath. 4, 7, 10, 13 gives 3, 3, 3.</p>"),
        ("Equal gaps means add or subtract",
         "<p>A constant difference means a linear sequence. Here the rule is \u201cadd 3\u201d, so "
         "the sequence continues 16, 19, 22.</p>"),
        ("Unequal gaps? Try dividing instead",
         "<p>2, 6, 18, 54 has growing gaps, but each term is 3 times the one before. The rule is "
         "\u201cmultiply by 3\u201d.</p>"),
        ("Still stuck? Look at the gaps between the gaps",
         "<p>1, 3, 6, 10, 15 has differences 2, 3, 4, 5 \u2014 increasing by one each time. Those "
         "are the triangular numbers.</p>"),
        ("State the rule precisely, in words",
         "<p>\u201cStart at 4 and add 3 each time\u201d is a complete rule. \u201cAdd 3\u201d on its "
         "own does not specify the sequence, because it never says where to begin.</p>"),
        ("Work backwards using the inverse",
         "<p>To step back one term in \u201cadd 3\u201d, subtract 3. The term before 4 is 1, and "
         "before that \u22122 \u2014 sequences carry on happily into negative numbers.</p>"),
    ],
    examples=[
        ("Continue: 5, 12, 19, 26, \u2026",
         ["Differences: 7, 7, 7.",
          "Rule: start at 5 and add 7.",
          "26 + 7 = 33, then 33 + 7 = 40."],
         "33, 40, 47"),
        ("Continue: 160, 80, 40, 20, \u2026",
         ["Differences are unequal (80, 40, 20), so try division.",
          "Each term is half the one before."],
         "10, 5, 2.5"),
        ("Find the missing term: 3, 8, ?, 18, 23",
         ["Known differences: 23 \u2212 18 = 5, and 8 \u2212 3 = 5.",
          "So the rule is add 5.",
          "8 + 5."],
         "13"),
        ("What are the next two triangular numbers after 15?",
         ["1, 3, 6, 10, 15 \u2014 differences 2, 3, 4, 5.",
          "The next difference is 6: 15 + 6 = 21.",
          "Then 7: 21 + 7 = 28."],
         "21 and 28"),
    ],
    mistakes=[
        ("Assuming every sequence adds.",
         "Check the differences first. If they grow or shrink, the rule probably multiplies or divides instead."),
        ("Giving the rule as \u2018add 3\u2019 without a starting point.",
         "A complete rule names the first term too: \u2018start at 4 and add 3\u2019."),
        ("Only checking the first gap.",
         "Test the rule against every pair you have. 2, 4, 8 could be \u2018add 2 then add 4\u2019 or \u2018double\u2019 \u2014 you need a third gap to decide."),
        ("Stopping at zero when counting backwards.",
         "Sequences continue through zero into negatives. The term before 1 in \u2018add 3\u2019 is \u22122."),
    ],
    sections=[
        ("Sequences worth recognising on sight",
         """<ul>
           <li><strong>Square numbers:</strong> 1, 4, 9, 16, 25 \u2014 the differences are the odd
           numbers 3, 5, 7, 9.</li>
           <li><strong>Triangular numbers:</strong> 1, 3, 6, 10, 15 \u2014 add 2, then 3, then 4.</li>
           <li><strong>Cube numbers:</strong> 1, 8, 27, 64, 125.</li>
           <li><strong>Fibonacci:</strong> 1, 1, 2, 3, 5, 8, 13 \u2014 each term is the sum of the
           two before it.</li>
           <li><strong>Powers of 2:</strong> 1, 2, 4, 8, 16, 32 \u2014 doubling.</li>
         </ul>
         <p>Spotting one of these instantly is worth a minute of staring at the differences.</p>"""),
        ("Position-to-term rules",
         """<p>Year 6 touches on describing a sequence by position. In 4, 7, 10, 13 the rule
         \u201cmultiply the position by 3 and add 1\u201d gives term 1 = 4, term 2 = 7 and term
         10 = 31 \u2014 without listing everything in between.</p>
         <p>The constant difference is always the multiplier, which is a useful shortcut: a sequence
         going up in 3s will always have a rule of the form 3n + something.</p>
         <p>At secondary this becomes the \u201cnth term\u201d, but the thinking is identical.</p>"""),
        ("Sequences in disguise",
         """<p>Pattern questions built from matchsticks or tiles are sequence questions wearing a
         costume. \u201cHow many sticks for 10 squares?\u201d \u2014 count the first few arrangements
         (4, 7, 10), find the difference (3), and apply the position rule (3n + 1, so 31).</p>
         <p>Encouraging children to tabulate the first three or four cases before reaching for a
         rule turns a confusing picture problem into an ordinary sequence.</p>"""),
    ],
    faqs=[
        ("What is a linear sequence?",
         "One where the same amount is added or subtracted each time, so the differences are constant. 4, 7, 10, 13 is linear."),
        ("How do I find the rule of a sequence?",
         "Write the differences between consecutive terms. Constant differences mean add or subtract; growing differences usually mean multiply."),
        ("Do primary children need the nth term?",
         "Not formally. Year 6 describes rules in words and uses position-to-term reasoning, but the algebraic nth term is Key Stage 3."),
        ("Can a sequence go down?",
         "Yes \u2014 20, 17, 14, 11 subtracts 3 each time, and it carries on into negative numbers."),
    ],
    cta=("Practise number sequences", "practice.html?year=6&level=medium"),
    related=["simple-algebra", "square-cube-numbers", "negative-numbers", "times-tables"],
),

# ---------------------------------------------------------------- 4
dict(
    slug="metric-units", cat=CAT, nav="Metric units & converting", read=5,
    h1="Metric units and how to convert them",
    card="mm, cm, m, km, g, kg, ml and litres \u2014 every conversion is a place-value shift.",
    years="Years 3\u20136",
    seo="Metric units explained \u2014 converting length, mass and capacity | Math It!",
    desc="The metric units children need, the conversion factors to memorise, how every conversion is a power-of-ten shift, and the imperial approximations on the KS2 curriculum.",
    keywords="metric units, converting units, cm to m, g to kg, ml to litres, metric conversions KS2, year 5 measures, imperial conversions",
    intro="""<p>The metric system is built on tens, which means every conversion is a place-value
      shift rather than a multiplication you have to think hard about. Converting 2.4 km to metres
      is the same operation as multiplying by 1,000 \u2014 shifting the digits three columns
      left.</p>
      <p>There are only about eight facts to know, and every one of them follows one of three
      patterns: \u00d7 10, \u00d7 100 or \u00d7 1,000.</p>""",
    steps=[
        ("Learn the prefixes",
         "<p><strong>milli-</strong> means a thousandth, <strong>centi-</strong> a hundredth and "
         "<strong>kilo-</strong> a thousand. So a millimetre is a thousandth of a metre, and a "
         "kilogram is a thousand grams.</p>"),
        ("Memorise the eight conversions",
         "<p>10 mm = 1 cm. 100 cm = 1 m. 1,000 mm = 1 m. 1,000 m = 1 km. 1,000 g = 1 kg. "
         "1,000 kg = 1 tonne. 1,000 ml = 1 litre. 1 ml = 1 cm\u00b3.</p>"),
        ("Decide whether the answer gets bigger or smaller",
         "<p>Going to a <em>smaller</em> unit means you need <em>more</em> of them, so multiply. "
         "Going to a bigger unit means fewer, so divide. Say this out loud before calculating.</p>"),
        ("Shift the digits",
         "<p>\u00d7 1,000 moves the digits three columns left; \u00f7 1,000 moves them three right. "
         "No written multiplication is ever needed.</p>"),
        ("Keep the unit attached to the number",
         "<p>An answer of \u201c2,400\u201d is incomplete. \u201c2,400 m\u201d is the answer.</p>"),
    ],
    examples=[
        ("Convert 2.4 km to metres.",
         ["km \u2192 m goes to a smaller unit, so multiply.",
          "1 km = 1,000 m, so \u00d7 1,000.",
          "Shift the digits three places left."],
         "2,400 m"),
        ("Convert 450 g to kilograms.",
         ["g \u2192 kg goes to a bigger unit, so divide.",
          "1,000 g = 1 kg, so \u00f7 1,000.",
          "Shift the digits three places right."],
         "0.45 kg"),
        ("Convert 7.5 cm to millimetres.",
         ["cm \u2192 mm is a smaller unit, so multiply by 10.",
          "Shift one place left."],
         "75 mm"),
        ("Add 1.2 litres and 650 ml.",
         ["Convert to the same unit first. 1.2 l = 1,200 ml.",
          "1,200 + 650 = 1,850 ml.",
          "Or expressed in litres: 1.85 l."],
         "1,850 ml (1.85 l)"),
    ],
    mistakes=[
        ("Multiplying when you should divide.",
         "Ask whether the answer ought to be a bigger or a smaller number first. 450 g in kilograms must be less than 1, so you divide."),
        ("Adding quantities that are in different units.",
         "1.2 l + 650 ml is not 651.2 of anything. Convert to a common unit before calculating."),
        ("Confusing centi- and milli-.",
         "Centi- is a hundredth (100 cm in a metre); milli- is a thousandth (1,000 mm in a metre). A centimetre is the bigger one."),
        ("Dropping the unit from the final answer.",
         "Measurement answers are wrong without units, and marks are routinely lost for this alone."),
    ],
    sections=[
        ("Area and volume units behave differently",
         """<p>This catches almost everybody. 1 m = 100 cm, but 1 m\u00b2 is
         <strong>10,000</strong> cm\u00b2, because a square metre is 100 cm by 100 cm.</p>
         <p>Similarly 1 m\u00b3 = 1,000,000 cm\u00b3. The rule: square the conversion factor for
         areas and cube it for volumes. Primary rarely tests this directly, but it is worth knowing
         why 1 m\u00b2 is not 100 cm\u00b2.</p>"""),
        ("Imperial approximations on the curriculum",
         """<p>Year 6 is expected to know rough equivalences between metric and imperial units:</p>
         <ul>
           <li>1 inch \u2248 2.5 cm</li>
           <li>1 foot \u2248 30 cm</li>
           <li>1 mile \u2248 1.6 km (so 5 miles \u2248 8 km)</li>
           <li>1 pound \u2248 450 g</li>
           <li>1 pint \u2248 568 ml, usually rounded to 570 ml</li>
           <li>1 gallon \u2248 4.5 litres</li>
         </ul>
         <p>These are approximations by design. Exam questions will say \u201cabout\u201d, or give
         the conversion factor in the question.</p>"""),
        ("Time is the odd one out",
         """<p>Time is not metric and never will be. 60 seconds in a minute, 60 minutes in an hour,
         24 hours in a day, 7 days in a week \u2014 none of these are powers of ten, which is why
         time calculations need a different approach, usually counting on through the next whole
         hour rather than subtracting.</p>
         <p>2 hours 45 minutes plus 1 hour 30 minutes: add the hours (3), add the minutes (75), then
         exchange 60 minutes for an hour. Answer: 4 hours 15 minutes.</p>"""),
    ],
    faqs=[
        ("How many centimetres are there in a metre?",
         "100. And 1,000 millimetres in a metre, since there are 10 mm in each centimetre."),
        ("Is 1 ml really the same as 1 cm\u00b3?",
         "Yes, exactly. A litre is defined as 1,000 cm\u00b3, which makes a millilitre exactly one cubic centimetre."),
        ("Do children need imperial units?",
         "Only the rough equivalences in Year 6 \u2014 miles to kilometres, pints to litres and so on. Calculations themselves are always set in metric."),
        ("What is the easiest way to remember which way to convert?",
         "A smaller unit means a bigger number. 1 m is 100 cm, so converting metres to centimetres makes the number larger."),
    ],
    cta=("Practise unit conversions", "practice.html?year=5&level=medium"),
    related=["powers-of-ten", "decimals-explained", "place-value", "simple-algebra"],
),

]
