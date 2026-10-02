# -*- coding: utf-8 -*-
"""Guides: Decimals and percentages."""

CAT = "Decimals & percentages"

GUIDES = [

# ---------------------------------------------------------------- 1
dict(
    slug="decimals-explained", cat=CAT, nav="Decimals explained", read=5,
    h1="Decimals explained",
    card="Tenths, hundredths and thousandths \u2014 and why 0.4 beats 0.38.",
    years="Years 4\u20136",
    seo="Decimals explained \u2014 tenths, hundredths and comparing | Math It!",
    desc="What decimal places mean, how to compare and order decimals, rounding them, and how decimals connect to fractions and money.",
    keywords="decimals explained, decimal place value, tenths hundredths, comparing decimals, ordering decimals, KS2 decimals, year 5 decimals",
    intro="""<p>A decimal extends place value past the ones column. The first digit after the point is
      tenths, the second is hundredths, the third is thousandths \u2014 each one ten times smaller
      than the one before.</p>
      <p>So 0.36 means 3 tenths and 6 hundredths. The decimal point is not a separator between two
      numbers; it is a marker showing where the ones column ends.</p>""",
    steps=[
        ("Name the columns after the point",
         "<p>Tenths, hundredths, thousandths. So 4.275 is 4 ones, 2 tenths, 7 hundredths and "
         "5 thousandths.</p>"),
        ("Read the digits individually",
         "<p>0.36 is \u201cnought point three six\u201d, not \u201cnought point thirty-six\u201d. "
         "Reading it as thirty-six invites the idea that it is bigger than 0.4.</p>"),
        ("Compare column by column, left to right",
         "<p>Start at the tenths. 0.4 vs 0.38: 4 tenths beats 3 tenths, so 0.4 wins. The number of "
         "digits is irrelevant.</p>"),
        ("Pad with zeros to make comparison easy",
         "<p>Write 0.4 as 0.40 and the comparison with 0.38 becomes obvious. Trailing zeros after "
         "the point change nothing.</p>"),
        ("Connect to fractions",
         "<p>0.1 = 1/10, 0.25 = 25/100 = 1/4, 0.75 = 3/4. Knowing the common conversions makes "
         "decimal questions much faster.</p>"),
    ],
    examples=[
        ("Put 0.7, 0.07, 0.77 and 0.707 in order, smallest first.",
         ["Pad to three decimal places: 0.700, 0.070, 0.770, 0.707.",
          "Compare the tenths: 7, 0, 7, 7 \u2014 so 0.07 is smallest.",
          "Among the rest compare hundredths: 0, 7, 0.",
          "Then thousandths separate 0.700 and 0.707."],
         "0.07, 0.7, 0.707, 0.77"),
        ("What is the 8 worth in 3.185?",
         ["First place after the point is tenths (1).",
          "Second is hundredths \u2014 that is the 8."],
         "8 hundredths, or 0.08"),
        ("Write 3/8 as a decimal.",
         ["A fraction is a division: 3 \u00f7 8.",
          "Short division: 8 into 30 is 3 remainder 6; 8 into 60 is 7 remainder 4; 8 into 40 is 5."],
         "0.375"),
    ],
    mistakes=[
        ("Thinking 0.38 &gt; 0.4 because 38 &gt; 4.",
         "Compare place by place from the left. 3 tenths is less than 4 tenths, and the extra digit is worth nothing to the comparison."),
        ("Reading 2.5 metres as \u2018two metres five centimetres\u2019.",
         "2.5 m is two and a half metres \u2014 250 cm. The digits after the point are fractions of the unit, not a second unit."),
        ("Thinking 0.50 is bigger than 0.5.",
         "They are identical. Trailing zeros after the decimal point add no value, though they can signal precision."),
        ("Lining up the left-hand digits when adding decimals.",
         "Line up the decimal points. Always."),
    ],
    sections=[
        ("Decimals and money",
         """<p>Money is the decimal most children meet first: \u00a33.45 is three pounds and 45
         hundredths of a pound. The habit of always writing two decimal places for money is useful
         in context but misleading in general \u2014 children start believing decimals always have
         exactly two places.</p>
         <p>Deliberately mix money questions with measurement questions, where 2.5 m and 0.375 kg
         are normal, to break that assumption.</p>"""),
        ("Recurring decimals",
         """<p>Some fractions do not terminate. 1/3 = 0.333\u2026, written 0.3 with a dot above the 3.
         1/7 = 0.142857142857\u2026, repeating in a block of six.</p>
         <p>Primary children only need to recognise that this happens and round appropriately. The
         reason, for the curious: a fraction terminates only if its simplified denominator is built
         from 2s and 5s, because those are the factors of 10.</p>"""),
        ("The conversions worth memorising",
         """<p>Ten pairs that between them cover most questions:</p>
         <p class="font-mono">1/2 = 0.5 \u00b7 1/4 = 0.25 \u00b7 3/4 = 0.75 \u00b7 1/5 = 0.2 \u00b7
         2/5 = 0.4 \u00b7 1/8 = 0.125 \u00b7 3/8 = 0.375 \u00b7 1/10 = 0.1 \u00b7 1/3 \u2248 0.333 \u00b7
         1/100 = 0.01</p>
         <p>Knowing these turns \u201cwhat is 0.75 of 60?\u201d into \u201cthree quarters of
         60\u201d, which is a mental calculation.</p>"""),
    ],
    faqs=[
        ("How many decimal places do children need at primary?",
         "Up to three by Year 6 \u2014 tenths, hundredths and thousandths \u2014 including comparing, ordering, rounding and calculating with them."),
        ("Why is 0.5 the same as 0.50?",
         "The trailing zero sits in the hundredths column and is worth zero hundredths. It adds nothing to the value, though it can indicate measurement precision."),
        ("How do I turn a fraction into a decimal?",
         "Divide the numerator by the denominator using short division. 3/8 is 3 \u00f7 8 = 0.375."),
        ("What is the decimal point actually for?",
         "It marks the boundary between whole units and parts of a unit. The ones column is immediately to its left."),
    ],
    cta=("Practise decimal questions", "practice.html?year=5&level=medium"),
    related=["place-value", "powers-of-ten", "multiplying-decimals", "fractions-decimals-percentages"],
),

# ---------------------------------------------------------------- 2
dict(
    slug="powers-of-ten", cat=CAT, nav="Multiplying by 10, 100, 1000", read=5,
    h1="Multiplying and dividing by 10, 100 and 1,000",
    card="The digits move, the point stays \u2014 and why \u2018add a zero\u2019 is bad advice.",
    years="Years 4\u20136",
    seo="Multiplying and dividing by 10, 100 and 1000 explained | Math It!",
    desc="How multiplying and dividing by powers of ten actually works, why \u2018add a zero\u2019 breaks with decimals, and how it makes metric conversions trivial.",
    keywords="multiplying by 10, dividing by 100, powers of ten, multiply by 1000, decimal point move, place value shift, KS2 multiplying by 10, year 5",
    intro="""<p>Multiplying by 10 makes every digit ten times bigger, so each one shifts one column to
      the left. Dividing by 10 does the reverse. 100 shifts two columns, 1,000 shifts three.</p>
      <p>Children are often taught \u201cadd a zero\u201d, which works for whole numbers and then
      collapses the moment decimals appear \u2014 3.6 \u00d7 10 is 36, not 3.60. Teaching the shift
      from the start avoids a reset in Year 5.</p>""",
    steps=[
        ("Count the zeros to get the shift",
         "<p>\u00d7 10 shifts one place, \u00d7 100 two places, \u00d7 1,000 three places.</p>"),
        ("Multiplying shifts digits left",
         "<p>Each digit becomes worth ten times more. 3.6 \u00d7 10: the 3 moves from ones to tens, "
         "the 6 from tenths to ones. Result 36.</p>"),
        ("Dividing shifts digits right",
         "<p>Each digit becomes worth ten times less. 450 \u00f7 100: the 4 moves from hundreds to "
         "ones, the 5 from tens to tenths. Result 4.5.</p>"),
        ("Fill empty columns with zeros",
         "<p>If shifting leaves a gap between the digits and the decimal point, a zero holds the "
         "place. 7 \u00d7 100 = 700; 7 \u00f7 100 = 0.07.</p>"),
        ("Keep the decimal point still",
         "<p>Picture the digits sliding past a fixed point rather than the point hopping along the "
         "digits. Both give the same answer, but the sliding image survives contact with 0.07.</p>"),
    ],
    examples=[
        ("3.6 \u00d7 100",
         ["Two zeros, so shift two places left.",
          "3 goes from ones to hundreds; 6 goes from tenths to tens.",
          "The empty ones column takes a zero."],
         "360"),
        ("45 \u00f7 1000",
         ["Three zeros, so shift three places right.",
          "4 goes from tens to hundredths; 5 from ones to thousandths.",
          "Zeros hold the ones and tenths columns."],
         "0.045"),
        ("0.07 \u00d7 1000",
         ["Shift three places left.",
          "The 7 moves from hundredths to tens."],
         "70"),
        ("Convert 2.4 km to metres.",
         ["1 km = 1,000 m, so multiply by 1,000.",
          "Shift three places left: 2 goes to thousands, 4 to hundreds."],
         "2,400 m"),
    ],
    mistakes=[
        ("\u2018Adding a zero\u2019 to multiply a decimal by 10.",
         "3.6 \u00d7 10 is 36, not 3.60. Shift the digits one column left instead \u2014 it works for every number."),
        ("Shifting the wrong way when dividing.",
         "Dividing makes numbers smaller, so digits move right. Check the answer is smaller than you started with."),
        ("Forgetting the placeholder zeros.",
         "7 \u00f7 100 = 0.07, not 0.7. Every empty column between the digits and the point needs a zero."),
        ("Counting the digits in 1,000 instead of the zeros.",
         "1,000 has three zeros, so three places. The leading 1 is not a shift."),
    ],
    sections=[
        ("Why the metric system is easy",
         """<p>Every metric conversion is a power-of-ten shift, which is why no multiplication is
         ever really needed:</p>
         <ul>
           <li>km \u2192 m: \u00d7 1,000</li>
           <li>m \u2192 cm: \u00d7 100</li>
           <li>cm \u2192 mm: \u00d7 10</li>
           <li>kg \u2192 g: \u00d7 1,000</li>
           <li>litres \u2192 ml: \u00d7 1,000</li>
         </ul>
         <p>Going the other way divides. A child who is fluent with place-value shifts can do every
         metric conversion on the KS2 curriculum without looking anything up \u2014 see
         <a href="metric-units.html" class="link">metric units</a>.</p>"""),
        ("Chaining shifts",
         """<p>Multiplying by 20 is \u00d7 2 then \u00d7 10. Multiplying by 300 is \u00d7 3 then
         \u00d7 100. Dividing by 50 is \u00f7 100 then \u00d7 2, or \u00f7 5 then \u00f7 10.</p>
         <p>This is how mental multiplication of larger numbers actually works, and it is far faster
         than reaching for a column method. 14 \u00d7 300 = 14 \u00d7 3 = 42, then shift twice =
         4,200.</p>"""),
        ("Checking with estimation",
         """<p>Place-value shift errors produce answers that are out by a factor of ten, which is
         exactly the kind of error estimation catches. If 2.4 km \u2018converts\u2019 to 240 m, a
         moment's thought says that is wrong \u2014 a kilometre is roughly a thousand paces, so 2.4
         km must be thousands of metres.</p>"""),
    ],
    faqs=[
        ("Does the decimal point move, or do the digits?",
         "Mathematically it does not matter, but teaching that the digits move keeps place value front and centre and avoids the \u2018add a zero\u2019 habit."),
        ("Why can't I just add a zero?",
         "It only works for whole numbers. For decimals it is wrong \u2014 3.6 \u00d7 10 is 36, and \u20183.60\u2019 is still 3.6."),
        ("How do I multiply by 10,000?",
         "Four zeros, so shift four places left. The pattern continues indefinitely."),
        ("What happens when you divide by 10 repeatedly?",
         "The number keeps getting smaller and the digits keep sliding right: 5, 0.5, 0.05, 0.005. It never reaches zero."),
    ],
    cta=("Practise multiplying and dividing by powers of ten", "practice.html?year=5&level=easy"),
    related=["place-value", "decimals-explained", "metric-units", "multiplying-decimals"],
),

# ---------------------------------------------------------------- 3
dict(
    slug="multiplying-decimals", cat=CAT, nav="Multiplying & dividing decimals", read=6,
    h1="Multiplying and dividing decimals",
    card="Ignore the point, calculate, then count the decimal places back in.",
    years="Years 5\u20136",
    seo="Multiplying and dividing decimals \u2014 the place-counting method | Math It!",
    desc="How to multiply decimals by counting decimal places, how to divide by a decimal by scaling both numbers up, and how to check with estimation.",
    keywords="multiplying decimals, dividing decimals, decimal multiplication, decimal places rule, divide by a decimal, KS2 decimals, year 6 decimals",
    intro="""<p>Multiplying decimals has a reliable two-part method: do the multiplication as if the
      decimal points were not there, then count how many decimal places the question contained and
      give the answer the same number.</p>
      <p>Dividing by a decimal works differently \u2014 you scale both numbers up until the divisor
      is a whole number, then divide normally.</p>""",
    steps=[
        ("Multiplying: strip the points out",
         "<p>4.2 \u00d7 0.3 becomes 42 \u00d7 3. Work with whole numbers, which you already know how "
         "to do.</p>"),
        ("Count the decimal places in the question",
         "<p>4.2 has one, 0.3 has one, so two in total.</p>"),
        ("Put the same number back into the answer",
         "<p>42 \u00d7 3 = 126, and two decimal places gives 1.26.</p>"),
        ("Dividing: make the divisor whole",
         "<p>For 7.2 \u00f7 0.4, multiply both numbers by 10: 72 \u00f7 4. Scaling both sides by the "
         "same amount leaves the answer unchanged.</p>"),
        ("Dividing by a whole number: keep the point in line",
         "<p>8.4 \u00f7 4 is short division with the decimal point written straight down from the "
         "dividend into the answer.</p>"),
        ("Estimate to check the magnitude",
         "<p>4.2 \u00d7 0.3 is about 4 \u00d7 0.3 = 1.2, so 1.26 is right and 12.6 is not.</p>"),
    ],
    examples=[
        ("4.2 \u00d7 0.3",
         ["Strip the points: 42 \u00d7 3 = 126.",
          "Decimal places in the question: 1 + 1 = 2.",
          "Place the point two from the right."],
         "1.26"),
        ("0.06 \u00d7 0.5",
         ["6 \u00d7 5 = 30.",
          "Decimal places: 2 + 1 = 3.",
          "Three places in 30 needs padding: 0.030."],
         "0.03"),
        ("7.2 \u00f7 0.4",
         ["Scale both by 10 so the divisor is whole: 72 \u00f7 4.",
          "Short division: 4 into 7 is 1 r 3; 4 into 32 is 8."],
         "18"),
        ("9.6 \u00f7 4",
         ["Divisor is already whole.",
          "Bring the decimal point straight up into the answer.",
          "4 into 9 is 2 r 1; 4 into 16 is 4."],
         "2.4"),
    ],
    mistakes=[
        ("Counting the decimal places in the intermediate answer rather than the question.",
         "The count comes from the two numbers you started with. 42 \u00d7 3 = 126 tells you nothing about where the point goes."),
        ("Forgetting to pad with zeros: writing 0.3 instead of 0.03 for 6 \u00d7 5 with three places.",
         "If the whole-number answer is too short, add leading zeros after the point until it has enough places."),
        ("Scaling only one side when dividing by a decimal.",
         "7.2 \u00f7 0.4 must become 72 \u00f7 4, not 72 \u00f7 0.4. Both numbers get multiplied by the same amount."),
        ("Expecting multiplication to make the number bigger.",
         "Multiplying by a decimal below 1 makes it smaller. 4.2 \u00d7 0.3 = 1.26, which is correct."),
    ],
    sections=[
        ("Why counting decimal places works",
         """<p>4.2 is 42 \u00f7 10 and 0.3 is 3 \u00f7 10. Multiplying them gives
         (42 \u00d7 3) \u00f7 100 = 126 \u00f7 100 = 1.26. The two divisions by ten combine into a
         division by a hundred, which is exactly two decimal places.</p>
         <p>In general, one decimal place means a hidden \u00f7 10, so the places simply add. Saying
         this once makes the rule memorable rather than arbitrary.</p>"""),
        ("Why scaling works for division",
         """<p>Division is a ratio. 7.2 \u00f7 0.4 asks how many 0.4s fit into 7.2. Make both ten
         times bigger and you are asking how many 4s fit into 72 \u2014 the same question, because
         both quantities grew by the same factor.</p>
         <p>This is identical to the equivalent-fractions idea: 7.2/0.4 = 72/4. Children who see the
         link tend to remember to scale both sides.</p>"""),
        ("Multiplying decimals by whole numbers",
         """<p>The commonest case in real life, and the easiest. 0.6 \u00d7 7: work out 6 \u00d7 7 =
         42, one decimal place in the question, so 4.2.</p>
         <p>It also responds well to mental methods. 0.6 \u00d7 7 is 6 tenths \u00d7 7 = 42 tenths =
         4.2 \u2014 no rule needed, just place value.</p>"""),
    ],
    faqs=[
        ("Where do I put the decimal point in the answer?",
         "Count the total decimal places in the numbers you multiplied, and give the answer that many. 4.2 \u00d7 0.3 has two, so 1.26."),
        ("Why does multiplying by 0.3 make the number smaller?",
         "Because 0.3 is less than one \u2014 you are taking three tenths of it, which is less than all of it."),
        ("How do I divide by a decimal?",
         "Multiply both numbers by 10, 100 or 1,000 until the divisor is a whole number, then divide as usual. The answer is unchanged."),
        ("Do I need to simplify a decimal answer?",
         "Drop meaningless trailing zeros \u2014 write 2.4, not 2.40 \u2014 unless the context is money, where two places is conventional."),
    ],
    cta=("Practise decimal multiplication and division", "practice.html?year=6&level=hard"),
    related=["powers-of-ten", "decimals-explained", "long-multiplication", "short-division"],
),

# ---------------------------------------------------------------- 4
dict(
    slug="percentages-of-amounts", cat=CAT, nav="Percentages of amounts", read=6,
    h1="Finding percentages of amounts",
    card="Build any percentage from 50%, 10%, 5% and 1% \u2014 no calculator needed.",
    years="Years 5\u20136",
    seo="How to find a percentage of an amount \u2014 the building-block method | Math It!",
    desc="Find any percentage of any number mentally by combining 50%, 25%, 10%, 5% and 1%. Includes increases, decreases and reverse percentage problems.",
    keywords="percentage of an amount, how to find percentages, 10 percent of, percentage increase, percentage decrease, KS2 percentages, year 6 percentages",
    intro="""<p>Per cent means \u201cper hundred\u201d. 35% is 35 out of every 100, or the fraction
      35/100.</p>
      <p>You almost never need to calculate that directly. Instead, build the percentage you want
      out of a few easy ones \u2014 50%, 25%, 10%, 5% and 1% \u2014 and add or subtract. It is faster
      than any formula and it works without a calculator.</p>""",
    steps=[
        ("Learn the five building blocks",
         "<p>50% = halve. 25% = halve twice. 10% = divide by 10. 5% = half of 10%. 1% = divide by "
         "100. Every other percentage is a combination.</p>"),
        ("Break the percentage into blocks",
         "<p>35% = 25% + 10%. Or 30% + 5%. Either works \u2014 pick whichever gives easier "
         "numbers.</p>"),
        ("Work out each block from the original amount",
         "<p>Always from the original, never from a running total.</p>"),
        ("Add them together",
         "<p>That is the answer.</p>"),
        ("For an increase or decrease, add or subtract from the whole",
         "<p>A 20% discount on \u00a380: 10% = 8, so 20% = 16, and you pay 80 \u2212 16 = \u00a364. "
         "Or go straight to 80% of 80 = 64.</p>"),
    ],
    examples=[
        ("Find 35% of 60.",
         ["10% of 60 = 6, so 30% = 18.",
          "5% is half of 10%, so 5% = 3.",
          "18 + 3."],
         "21"),
        ("Find 15% of \u00a380.",
         ["10% of 80 = 8.",
          "5% = 4.",
          "8 + 4."],
         "\u00a312"),
        ("A \u00a345 coat is reduced by 20%. What is the new price?",
         ["10% of 45 = 4.50, so 20% = 9.",
          "45 \u2212 9 = 36.",
          "Or directly: 80% of 45 = 4.50 \u00d7 8."],
         "\u00a336"),
        ("Find 1% of 350, then 3%.",
         ["1% means divide by 100: 350 \u00f7 100 = 3.5.",
          "3% is three lots of that."],
         "10.5"),
    ],
    mistakes=[
        ("Calculating the discount and giving it as the price.",
         "20% off \u00a380 is a \u00a316 discount and a \u00a364 price. Re-read what the question asked for."),
        ("Taking each percentage off the running total.",
         "All the blocks come from the <em>original</em> amount. 35% is 30% of the original plus 5% of the original."),
        ("Assuming a 20% rise then a 20% fall returns you to the start.",
         "It does not. \u00a3100 \u2192 \u00a3120 \u2192 \u00a396, because the fall is 20% of the larger number."),
        ("Dividing by the percentage.",
         "To find 25% of 80 you divide by 4, not by 25. Convert the percentage to a fraction first if that helps."),
    ],
    sections=[
        ("The fraction shortcut",
         """<p>Some percentages are much faster as fractions:</p>
         <p class="font-mono">50% = 1/2 \u00b7 25% = 1/4 \u00b7 75% = 3/4 \u00b7 20% = 1/5 \u00b7
         40% = 2/5 \u00b7 10% = 1/10 \u00b7 12.5% = 1/8 \u00b7 33\u2153% = 1/3</p>
         <p>\u201c75% of 48\u201d is three quarters of 48: divide by 4 to get 12, multiply by 3 to
         get 36. Far quicker than building from 10%.</p>"""),
        ("Reverse percentage problems",
         """<p>\u201cAfter a 20% discount a coat costs \u00a336. What was the original price?\u201d</p>
         <p>\u00a336 is 80% of the original. So 1% is 36 \u00f7 80 = 0.45, and 100% is 45. The
         original price was \u00a345.</p>
         <p>The trap is taking 20% of \u00a336 and adding it back, which gives \u00a343.20 \u2014
         wrong, because the 20% was of the larger original. Always find 1% of the known percentage
         first.</p>"""),
        ("Percentage change",
         """<p>To find a percentage change, work out the difference, divide by the
         <em>original</em>, and multiply by 100.</p>
         <p>A price rises from \u00a340 to \u00a350. The difference is \u00a310; 10 \u00f7 40 = 0.25;
         that is a 25% increase. Note it is not 20% \u2014 dividing by the new price is the standard
         error.</p>"""),
    ],
    faqs=[
        ("What is the quickest way to find 10%?",
         "Divide by 10 \u2014 shift every digit one place right. 10% of 46 is 4.6."),
        ("How do I find a percentage without a calculator?",
         "Build it from 50%, 25%, 10%, 5% and 1%. Almost every percentage in a primary question is a sum of two or three of those."),
        ("Is 'percentage of' the same as 'fraction of'?",
         "Yes. A percentage is a fraction with denominator 100, so the method is identical."),
        ("Why isn't a 20% rise cancelled by a 20% fall?",
         "Because the second percentage is taken from a different, larger amount. \u00a3100 rises to \u00a3120, and 20% of \u00a3120 is \u00a324, bringing it to \u00a396."),
    ],
    cta=("Practise percentage questions", "practice.html?year=6&level=medium"),
    related=["fractions-decimals-percentages", "fractions-of-amounts", "ratio-and-proportion", "decimals-explained"],
),

# ---------------------------------------------------------------- 5
dict(
    slug="fractions-decimals-percentages", cat=CAT, nav="Converting FDP", read=5,
    h1="Converting fractions, decimals and percentages",
    card="One quantity, three notations \u2014 and the conversion table worth memorising.",
    years="Years 5\u20136",
    seo="Converting between fractions, decimals and percentages | Math It!",
    desc="How to convert in all six directions between fractions, decimals and percentages, plus the standard conversion table every KS2 child should know by heart.",
    keywords="fractions decimals percentages, converting fractions to decimals, decimal to percentage, percentage to fraction, FDP conversion, KS2 FDP, year 6",
    intro="""<p>A half, 0.5 and 50% are the same quantity written three ways. Being able to move
      between them freely is one of the highest-value skills in upper primary, because it lets you
      pick whichever form makes a question easiest.</p>
      <p>There are six conversions. Three are trivial, and the other three are short division or a
      simplification.</p>""",
    steps=[
        ("Decimal to percentage: \u00d7 100",
         "<p>0.45 \u2192 45%. Shift the digits two places left.</p>"),
        ("Percentage to decimal: \u00f7 100",
         "<p>45% \u2192 0.45. Shift two places right.</p>"),
        ("Percentage to fraction: over 100, then simplify",
         "<p>45% \u2192 45/100 \u2192 9/20.</p>"),
        ("Fraction to percentage: scale to 100, or go via the decimal",
         "<p>3/5 \u2192 \u00d74 \u2192 60/100 \u2192 60%. If the denominator will not scale neatly to "
         "100, convert to a decimal first.</p>"),
        ("Fraction to decimal: divide",
         "<p>3/8 is 3 \u00f7 8 = 0.375 by short division.</p>"),
        ("Decimal to fraction: read the place value, then simplify",
         "<p>0.375 is 375 thousandths \u2192 375/1000 \u2192 3/8.</p>"),
    ],
    examples=[
        ("Convert 3/8 to a decimal and a percentage.",
         ["3 \u00f7 8 by short division: 8 into 30 is 3 r 6, 8 into 60 is 7 r 4, 8 into 40 is 5.",
          "So 0.375.",
          "\u00d7 100 for the percentage."],
         "0.375 and 37.5%"),
        ("Convert 24% to a fraction in its simplest form.",
         ["24% = 24/100.",
          "Both divide by 4."],
         "6/25"),
        ("Convert 0.6 to a fraction.",
         ["0.6 is 6 tenths = 6/10.",
          "Both divide by 2."],
         "3/5"),
        ("Put 0.7, 68% and 3/4 in order, smallest first.",
         ["Convert everything to percentages.",
          "0.7 = 70%. 3/4 = 75%.",
          "Compare 70, 68, 75."],
         "68%, 0.7, 3/4"),
    ],
    mistakes=[
        ("Shifting the wrong way between decimals and percentages.",
         "Percentages are the bigger-looking number. Going to a percentage multiplies by 100; going back divides."),
        ("Writing 0.45 as 45/100 and stopping.",
         "That is correct but not simplified. 45/100 = 9/20."),
        ("Converting 1/3 to 0.33 and calling it exact.",
         "1/3 = 0.333\u2026 recurring. Use the fraction when exactness matters, and round only at the end."),
        ("Comparing mixed notations directly.",
         "Convert everything to one form \u2014 usually percentages \u2014 before ordering. Comparing 0.7 with 68% by eye invites errors."),
    ],
    sections=[
        ("The table worth knowing by heart",
         """<table>
           <thead><tr><th>Fraction</th><th>Decimal</th><th>Percentage</th></tr></thead>
           <tbody>
             <tr><td>1/2</td><td>0.5</td><td>50%</td></tr>
             <tr><td>1/4</td><td>0.25</td><td>25%</td></tr>
             <tr><td>3/4</td><td>0.75</td><td>75%</td></tr>
             <tr><td>1/5</td><td>0.2</td><td>20%</td></tr>
             <tr><td>2/5</td><td>0.4</td><td>40%</td></tr>
             <tr><td>1/10</td><td>0.1</td><td>10%</td></tr>
             <tr><td>3/10</td><td>0.3</td><td>30%</td></tr>
             <tr><td>1/8</td><td>0.125</td><td>12.5%</td></tr>
             <tr><td>3/8</td><td>0.375</td><td>37.5%</td></tr>
             <tr><td>1/3</td><td>0.333\u2026</td><td>33\u2153%</td></tr>
             <tr><td>1/100</td><td>0.01</td><td>1%</td></tr>
           </tbody>
         </table>
         <p>Eleven rows. A child who knows these can answer most FDP questions on sight rather than
         calculating.</p>"""),
        ("Choosing the easiest form",
         """<p>The point of converting is to make a question easier:</p>
         <ul>
           <li>\u201cFind 75% of 48\u201d \u2192 use the fraction: three quarters of 48 = 36.</li>
           <li>\u201cWhich is bigger, 3/8 or 0.4?\u201d \u2192 use decimals: 0.375 vs 0.4.</li>
           <li>\u201cIncrease \u00a360 by 5%\u201d \u2192 use the percentage blocks directly.</li>
         </ul>
         <p>Fluency means not having a favourite \u2014 it means reading the question and picking.</p>"""),
        ("Ordering mixed lists",
         """<p>SATs reasoning papers love a list like \u201c0.7, 68%, 3/4, 0.68\u201d. The method is
         always the same: convert everything to one notation, order, then write the answer back in
         the original forms.</p>
         <p>Percentages are usually the best target because they turn everything into whole numbers
         you can compare at a glance.</p>"""),
    ],
    faqs=[
        ("How do I turn a fraction into a percentage?",
         "Scale the denominator to 100 if it divides neatly (3/5 = 60/100 = 60%), otherwise divide to get a decimal and multiply by 100."),
        ("What is 1/3 as a percentage?",
         "33\u2153%, or about 33.3%. It does not terminate, so any decimal version is rounded."),
        ("Which form should I give in an answer?",
         "Whichever the question asks for. If it does not say, match the form used in the question."),
        ("Why do these three topics get taught together?",
         "Because they are three notations for the same idea \u2014 a part of a whole. Teaching them separately makes children think they are three different topics with three sets of rules."),
    ],
    cta=("Practise FDP conversions", "practice.html?year=6&level=medium"),
    related=["percentages-of-amounts", "decimals-explained", "equivalent-fractions", "fractions-of-amounts"],
),

]
