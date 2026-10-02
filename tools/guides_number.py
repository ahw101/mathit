# -*- coding: utf-8 -*-
"""Guides: Number and place value."""

CAT = "Number & place value"

GUIDES = [

# ---------------------------------------------------------------- 1
dict(
    slug="place-value", cat=CAT, nav="Place value", read=6,
    h1="Place value: what each digit is actually worth",
    card="Why the 7 in 4,703 is worth 700, and how that one idea underpins every written method.",
    years="Years 2–6",
    seo="Place value explained — ones, tens, hundreds and decimals | Math It!",
    desc="Place value explained simply for primary school. What each digit in a number is worth, how to read large numbers, how the decimal columns work, and the mistakes that cause most arithmetic errors.",
    keywords="place value, place value explained, what is place value, hundreds tens ones, decimal place value, KS2 place value, year 4 place value",
    intro="""<p>Place value is the idea that a digit's worth depends on where it sits. The
      digit 7 is worth seven in 27, seventy in 74, and seven hundred in 4,703 — same symbol,
      three different values.</p>
      <p>It sounds almost too simple to be worth teaching, but nearly every arithmetic mistake a
      primary child makes traces back to it: columns lined up wrongly, a zero dropped, a decimal
      point drifting. Get place value secure and the written methods stop being arbitrary rules.</p>""",
    steps=[
        ("Name the columns",
         "<p>Reading right to left: ones, tens, hundreds, thousands, ten thousands, hundred "
         "thousands, millions. Each column is <strong>ten times</strong> the one to its right.</p>"),
        ("Read the number in groups of three",
         "<p>British convention groups digits in threes with a comma: 4,703 and 1,250,000. Read "
         "each group, then say its label. 1,250,000 is \u201cone million, two hundred and fifty "
         "thousand\u201d.</p>"),
        ("Partition it",
         "<p>Split the number into what each digit is worth: 4,703 = 4,000 + 700 + 0 + 3. This is "
         "the single most useful habit in primary maths and it is what column methods do "
         "automatically.</p>"),
        ("Keep going past the decimal point",
         "<p>The pattern does not stop at the ones column. Moving right, each column is "
         "<strong>ten times smaller</strong>: tenths, hundredths, thousandths. So 0.36 is "
         "3 tenths and 6 hundredths.</p>"),
        ("Treat zero as a placeholder, not a blank",
         "<p>The 0 in 4,703 is doing real work: it holds the tens column open so the 7 stays in "
         "the hundreds. Remove it and you get 473, a completely different number.</p>"),
    ],
    examples=[
        ("What is the 6 worth in 362,415?",
         ["Count the columns from the right: 5 ones, 1 ten, 4 hundreds, 2 thousands, "
          "6 ten thousands, 3 hundred thousands.",
          "The 6 is in the ten thousands column.",
          "Ten thousands means 6 \u00d7 10,000."],
         "60,000"),
        ("Write \u201cfour thousand and nine\u201d in digits.",
         ["Four thousand gives a 4 in the thousands column.",
          "Nine gives a 9 in the ones column.",
          "Nothing was said about hundreds or tens, so both need a zero to hold the places open."],
         "4,009"),
        ("Which is bigger, 0.4 or 0.38?",
         ["Do not compare digit counts \u2014 0.38 having more digits means nothing.",
          "Line up the decimal points and fill with zeros: 0.40 and 0.38.",
          "4 tenths beats 3 tenths."],
         "0.4 is bigger"),
    ],
    mistakes=[
        ("Reading 0.38 as \u201cnought point thirty-eight\u201d and assuming it beats 0.4 because 38 &gt; 4.",
         "Read it as \u201cnought point three eight\u201d and compare column by column, starting from the tenths."),
        ("Writing \u201cthree thousand and twenty\u201d as 300020.",
         "Say the number in groups of three first, then count how many columns you actually need: 3,020."),
        ("Lining up column addition from the left when the numbers are different lengths.",
         "Always line up the <em>ones</em> column, or the decimal point. Add leading or trailing zeros if it helps."),
        ("Thinking a digit \u201cmoves\u201d when you multiply by 10 and the number stays put.",
         "The digits move left; the decimal point stays where it is. 3.6 \u00d7 10 = 36 because the 3 and the 6 each shift one column left."),
    ],
    sections=[
        ("How far does the pattern go?",
         """<p>A long way in both directions, and that is the point. Primary children meet numbers to
         ten million by Year 6 and decimals to three places. The naming changes but the structure
         does not: every step left multiplies by ten, every step right divides by ten.</p>
         <p>That is also why the metric system is easy and imperial is not. Converting 2.4 km to
         metres is a place-value shift (2,400 m). Converting 2.4 miles to yards is a multiplication
         you have to look up.</p>"""),
        ("Rounding, comparing and ordering all run on place value",
         """<p>Rounding asks \u201cwhich multiple of 10, or 100, or 0.1 is this closest to?\u201d You
         cannot answer that without knowing which column you are rounding to. Comparing two numbers
         means walking left to right until the digits differ. Ordering a list means doing that
         repeatedly.</p>
         <p>If a child can confidently say what each digit is worth, those three skills arrive almost
         free. If they cannot, each one has to be learned as a separate trick \u2014 and tricks fail
         under pressure.</p>"""),
        ("A quick diagnostic",
         """<p>Ask these four questions. A child who answers all four has secure place value.</p>
         <ul>
           <li>What is the 5 worth in 25,106?</li>
           <li>Write one hundred thousand and sixty in digits.</li>
           <li>What is 7.2 \u00d7 100?</li>
           <li>Put these in order: 0.7, 0.07, 0.77, 0.707.</li>
         </ul>
         <p>Answers: 5,000; 100,060; 720; and 0.07, 0.7, 0.707, 0.77.</p>"""),
    ],
    faqs=[
        ("At what age should place value be secure?",
         "Three-digit numbers by the end of Year 3, four digits by Year 4, and numbers to ten million plus three decimal places by the end of Year 6. In practice it is worth re-checking every year \u2014 it decays quickly without use."),
        ("Why do we use a comma in 4,703 but not in 4703?",
         "Both are correct. UK schools usually introduce the comma separator for five digits and up, and it genuinely helps reading. Spreadsheets and exam papers vary, so children should be comfortable with either."),
        ("Is the decimal point part of place value?",
         "Yes \u2014 it is just the marker showing where the ones column ends. Columns continue to the right as tenths, hundredths and thousandths, each ten times smaller than the last."),
        ("My child can say the columns but still makes column-addition errors. Why?",
         "Usually because they are reciting the names rather than using them. Have them partition each number aloud (\u201c4,703 is 4,000 and 700 and 3\u201d) before writing anything down."),
    ],
    cta=("Practise place value questions", "practice.html?year=4&level=medium"),
    related=["rounding", "negative-numbers", "powers-of-ten", "decimals-explained"],
),

# ---------------------------------------------------------------- 2
dict(
    slug="rounding", cat=CAT, nav="Rounding", read=5,
    h1="Rounding numbers without guessing",
    card="Round to 10, 100, 1,000 or any number of decimal places \u2014 and know what to do with a 5.",
    years="Years 4\u20136",
    seo="How to round numbers \u2014 to 10, 100, 1,000 and decimal places | Math It!",
    desc="How to round to the nearest 10, 100, 1,000 or to a given number of decimal places. The underline-the-digit method, what to do when the next digit is a 5, and why 9s cause chaos.",
    keywords="rounding numbers, round to nearest 10, round to nearest 100, rounding decimals, round to 2 decimal places, KS2 rounding, year 5 rounding",
    intro="""<p>Rounding replaces a number with a nearby, tidier one. It is how you estimate a shopping
      bill, sanity-check a long calculation, or report a measurement honestly.</p>
      <p>Most children can round 47 to 50. Things fall apart with 2,495 to the nearest hundred, or
      3.96 to one decimal place, because those involve a 9 rolling over. The method below handles
      all of it without needing a number line.</p>""",
    steps=[
        ("Decide which column you are rounding to",
         "<p>Nearest 10? Nearest 1,000? Two decimal places? Find that column and underline its "
         "digit. This is the digit that may change.</p>"),
        ("Look at the single digit immediately to its right",
         "<p>Only that one. Not the rest of the number. In 2,4<u>4</u>9 rounded to the nearest "
         "hundred, the underlined digit is the 4 in the hundreds and the decider is the 4 in the "
         "tens.</p>"),
        ("Below 5 rounds down, 5 or above rounds up",
         "<p>\u201cRounds down\u201d means the underlined digit stays as it is. \u201cRounds up\u201d "
         "means it increases by one.</p>"),
        ("Clear out everything to the right",
         "<p>For whole numbers, replace the following digits with zeros \u2014 they are placeholders "
         "and you must keep them. For decimals, simply delete them.</p>"),
        ("Handle a 9 by carrying",
         "<p>If the underlined digit is a 9 and it rounds up, it becomes 0 and you carry 1 into the "
         "next column left, exactly like column addition. 3.9<u>6</u> to one decimal place: the 9 "
         "becomes 10, so you get 4.0.</p>"),
    ],
    examples=[
        ("Round 2,449 to the nearest hundred.",
         ["Hundreds digit is 4 (2,4<u>4</u>9).",
          "The decider is the next digit right: 4.",
          "4 is below 5, so the hundreds digit stays as 4.",
          "Tens and ones become zeros."],
         "2,400"),
        ("Round 2,450 to the nearest hundred.",
         ["Hundreds digit is 4. The decider is 5.",
          "5 or above rounds up, so 4 becomes 5.",
          "Everything to the right becomes zero."],
         "2,500"),
        ("Round 3.96 to one decimal place.",
         ["One decimal place means the tenths column: the 9.",
          "The decider is the 6 in the hundredths \u2014 that rounds up.",
          "9 + 1 = 10, so write 0 in the tenths and carry 1 into the ones: 3 becomes 4.",
          "Keep the trailing zero \u2014 it shows you rounded to one decimal place."],
         "4.0"),
        ("Round 148,672 to the nearest 10,000.",
         ["Ten-thousands digit is 4 (1<u>4</u>8,672).",
          "Decider is the 8 in the thousands \u2014 rounds up.",
          "4 becomes 5, and all five digits to the right become zeros."],
         "150,000"),
    ],
    mistakes=[
        ("Rounding in stages: 2,449 \u2192 2,450 \u2192 2,500.",
         "Round once, in a single step, straight to the target column. Staged rounding inflates numbers."),
        ("Looking at the whole tail: \u201c449 is nearly 500 so it rounds up\u201d.",
         "Only the single digit to the right of the target column decides. 449 rounds the hundreds down."),
        ("Dropping the placeholder zeros, turning 2,400 into 24.",
         "For whole numbers the zeros are essential \u2014 they hold the place value. Only decimals lose their tail."),
        ("Writing 4 instead of 4.0 when rounding 3.96 to one decimal place.",
         "If the question asks for one decimal place, give one decimal place. The trailing zero is information."),
    ],
    sections=[
        ("Why 5 rounds up",
         """<p>5 is exactly halfway, so there is no mathematically forced answer \u2014 it is a
         convention. UK schools use \u201cround half up\u201d because it is easy to state and easy to
         check. Statisticians sometimes use \u201cround half to even\u201d (banker's rounding) so that
         errors cancel over thousands of values, but your child will never be marked on that at
         primary level.</p>"""),
        ("Rounding to estimate",
         """<p>The real reason rounding is on the curriculum is estimation. Before working out
         48 \u00d7 31, round to 50 \u00d7 30 = 1,500. Now you know the answer should be near 1,500, so
         an answer of 148 or 14,880 is clearly a slipped decimal point or a missed column.</p>
         <p>Teach it as a reflex: estimate, calculate, compare. It catches more errors than checking
         the working does, and it is far faster.</p>"""),
        ("Significant figures \u2014 a preview",
         """<p>Secondary school adds rounding to significant figures, which counts from the first
         non-zero digit rather than from the decimal point. 0.004836 to two significant figures is
         0.0048. The underline-and-decide method is identical; only the choice of column changes.
         Children with a secure rounding method pick it up in minutes.</p>"""),
    ],
    faqs=[
        ("Does 0.5 round to 0 or 1?",
         "To 1, using the standard UK school convention that 5 rounds up."),
        ("How do I round a negative number?",
         "Round the size of the number and keep the sign. \u22122.4 to the nearest whole number is \u22122; \u22122.6 is \u22123. Strictly \u22122.5 rounds to \u22122 under \u2018half up\u2019, but primary questions avoid that case."),
        ("What does \u2018to the nearest whole number\u2019 mean?",
         "Round to zero decimal places \u2014 look at the tenths digit to decide. 7.5 becomes 8, 7.49 becomes 7."),
        ("Why does my child's answer differ from the calculator's?",
         "Usually staged rounding, or rounding partway through a calculation. Always work with the full number and round only the final answer."),
    ],
    cta=("Practise rounding and estimating", "practice.html?year=5&level=medium"),
    related=["place-value", "decimals-explained", "powers-of-ten", "mental-strategies"],
),

# ---------------------------------------------------------------- 3
dict(
    slug="negative-numbers", cat=CAT, nav="Negative numbers", read=6,
    h1="Negative numbers: counting below zero",
    card="Temperatures, bank balances and number lines \u2014 how to add and subtract through zero.",
    years="Years 4\u20136",
    seo="Negative numbers explained \u2014 adding, subtracting and ordering | Math It!",
    desc="Negative numbers explained for primary school. How to order them, count through zero, work out differences, and handle the two minus signs that confuse everybody.",
    keywords="negative numbers, negative numbers KS2, adding negative numbers, subtracting negative numbers, number line negative, temperature maths, year 5 negative numbers",
    intro="""<p>Negative numbers are the numbers below zero: \u22121, \u22122, \u22123 and so on. Children
      meet them first as temperatures, then as floors below ground in a lift, then as overdrawn bank
      balances.</p>
      <p>The arithmetic itself is not hard. What trips people up is that the minus sign does two
      different jobs \u2014 it marks a negative number, and it means \u201csubtract\u201d. Separating
      those two uses is most of the battle.</p>""",
    steps=[
        ("Picture the number line",
         "<p>\u2026 \u22125, \u22124, \u22123, \u22122, \u22121, 0, 1, 2, 3 \u2026 Negative numbers run "
         "to the left of zero. Everything that follows is just movement along this line.</p>"),
        ("Bigger looks smaller",
         "<p>\u22127 is <em>less</em> than \u22122, even though 7 is bigger than 2. Further left means "
         "smaller. On a thermometer, \u22127\u00b0C is colder.</p>"),
        ("Adding moves right, subtracting moves left",
         "<p>Start at the first number and step. \u22123 + 5: start at \u22123, move 5 right, land on 2. "
         "4 \u2212 9: start at 4, move 9 left, land on \u22125.</p>"),
        ("Difference means the gap",
         "<p>The difference between \u22124 and 3 is the distance along the line: 4 steps up to zero, "
         "then 3 more. That is 7. Add the two sizes when the numbers are on opposite sides of "
         "zero.</p>"),
        ("Two minuses together make a plus",
         "<p>5 \u2212 (\u22123) means \u201cstart at 5 and take away a debt of 3\u201d, which leaves you "
         "better off: 5 + 3 = 8. Subtracting a negative always moves you right.</p>"),
    ],
    examples=[
        ("The temperature is \u22126\u00b0C and rises by 9 degrees. What is it now?",
         ["Start at \u22126 on the line.",
          "Rising means moving right, 9 steps.",
          "6 steps take you to 0, with 3 steps left over."],
         "3\u00b0C"),
        ("What is the difference between \u22128 and \u22123?",
         ["Both are on the same side of zero.",
          "From \u22128 to \u22123 is 5 steps right.",
          "Same side of zero \u2192 subtract the sizes: 8 \u2212 3."],
         "5"),
        ("Work out \u22127 + 12 \u2212 4.",
         ["Left to right. Start at \u22127.",
          "+12 moves right: \u22127 + 12 = 5.",
          "\u22124 moves left: 5 \u2212 4 = 1."],
         "1"),
        ("Work out 2 \u2212 (\u22126).",
         ["The brackets show \u22126 is a negative number, not a second subtraction.",
          "Subtracting a negative reverses direction \u2014 you move right.",
          "2 + 6."],
         "8"),
    ],
    mistakes=[
        ("Saying \u22127 is bigger than \u22122 because 7 is bigger than 2.",
         "Compare positions, not sizes. Further left is always smaller, so \u22127 &lt; \u22122."),
        ("Counting zero as a step when crossing it.",
         "From \u22122 to 3 is 5 steps, not 6. Zero is a position you pass through, not a step."),
        ("Treating 5 \u2212 (\u22123) as 5 \u2212 3.",
         "Subtracting a negative adds. 5 \u2212 (\u22123) = 8. If you can, rewrite it with the double sign removed before calculating."),
        ("Assuming the answer to a subtraction must be positive.",
         "3 \u2212 10 is perfectly valid and equals \u22127. Nothing says the bigger number has to go first."),
    ],
    sections=[
        ("Contexts that make it obvious",
         """<p>Abstract number lines work for some children; contexts work for the rest. The three
         that carry the most weight:</p>
         <ul>
           <li><strong>Temperature.</strong> \u201cIt was \u22124\u00b0C overnight and rose 11 degrees
           by noon.\u201d Natural, and the rise/fall language maps directly onto right/left.</li>
           <li><strong>Lifts and floors.</strong> Level \u22122 is two floors below ground. Going up
           three floors from \u22122 lands on 1.</li>
           <li><strong>Money.</strong> A balance of \u2212\u00a330 means you owe \u00a330. Pay in
           \u00a350 and you have \u00a320.</li>
         </ul>"""),
        ("What primary children are and are not expected to do",
         """<p>The National Curriculum asks Year 4 to count backwards through zero, Year 5 to
         interpret negative numbers in context and count forwards and backwards with positive and
         negative whole numbers including through zero, and Year 6 to use negative numbers in
         context and calculate intervals across zero.</p>
         <p>Multiplying and dividing negatives \u2014 the \u201ctwo negatives make a positive\u201d rule
         for \u22123 \u00d7 \u22124 \u2014 is secondary work. Do not rush it; a child who is secure with
         ordering and intervals is exactly where they should be.</p>"""),
        ("A reliable drawing",
         """<p>When a child is stuck, have them draw the line and mark zero in the middle before
         doing anything else. Nine times out of ten the error was a direction error, and the drawing
         makes direction impossible to get wrong. It is slow, but speed comes later and only after
         the method is right.</p>"""),
    ],
    faqs=[
        ("Is zero positive or negative?",
         "Neither. Zero is the boundary between them. It is an even number, but it has no sign."),
        ("How do I write negative numbers properly?",
         "With a short dash immediately before the digits and no space: \u22125, not \u2212 5. Some books raise it slightly (\u207b5) to distinguish it from subtraction, but that is not required."),
        ("When do children multiply negative numbers?",
         "Normally Year 7 or 8. Primary stops at ordering, counting through zero and finding intervals."),
        ("What is the difference between \u22125 and 5?",
         "10. They sit the same distance either side of zero, so the gap is 5 + 5."),
    ],
    cta=("Practise negative number questions", "practice.html?year=6&level=medium"),
    related=["place-value", "column-subtraction", "number-sequences", "mental-strategies"],
),

# ---------------------------------------------------------------- 4
dict(
    slug="factors-multiples-primes", cat=CAT, nav="Factors, multiples & primes", read=7,
    h1="Factors, multiples and prime numbers",
    card="Tell them apart for good, find factor pairs systematically, and learn the primes to 100.",
    years="Years 4\u20136",
    seo="Factors, multiples and prime numbers explained | Math It!",
    desc="The difference between factors and multiples, how to list factor pairs without missing any, what makes a number prime, and the primes to 100 worth knowing by heart.",
    keywords="factors and multiples, prime numbers, factor pairs, common factors, lowest common multiple, prime numbers to 100, KS2 factors, year 5 primes",
    intro="""<p>Factors divide into a number. Multiples come out of it. 3 is a factor of 12; 12 is a
      multiple of 3. The two words describe the same relationship from opposite ends, which is
      precisely why children mix them up.</p>
      <p>Prime numbers are the ones with exactly two factors: themselves and 1. They matter because
      every other whole number is built by multiplying primes together \u2014 and because simplifying
      fractions gets much faster once you can spot them.</p>""",
    steps=[
        ("Fix the vocabulary first",
         "<p><strong>Factors</strong> are smaller (or equal) and divide in exactly. "
         "<strong>Multiples</strong> are bigger (or equal) and are what you land on when counting "
         "up in that number. A number has a finite list of factors and an infinite list of "
         "multiples.</p>"),
        ("Find factors in pairs, starting from 1",
         "<p>For 36: 1 \u00d7 36, 2 \u00d7 18, 3 \u00d7 12, 4 \u00d7 9, 6 \u00d7 6. Work up through 1, 2, "
         "3, 4\u2026 and stop when the pair meets in the middle. Pairing guarantees you miss "
         "nothing.</p>"),
        ("Use the divisibility tests",
         "<p>2: even. 3: digits add to a multiple of 3. 4: last two digits divide by 4. 5: ends in "
         "0 or 5. 6: passes 2 and 3. 9: digits add to a multiple of 9. 10: ends in 0.</p>"),
        ("Check for prime",
         "<p>A number is prime if it has exactly two factors. Test by dividing by 2, 3, 5, 7, 11\u2026 "
         "and you only need to go as far as the square root. For 97, testing up to 9 is enough.</p>"),
        ("Common factors and common multiples",
         "<p>List both sets and look for overlap. The <strong>highest common factor</strong> (HCF) "
         "simplifies fractions; the <strong>lowest common multiple</strong> (LCM) gives you a common "
         "denominator.</p>"),
    ],
    examples=[
        ("List all the factors of 48.",
         ["1 \u00d7 48, 2 \u00d7 24, 3 \u00d7 16, 4 \u00d7 12, 6 \u00d7 8.",
          "5 does not divide 48; 7 does not either.",
          "After 6 \u00d7 8 the next pair would repeat, so stop."],
         "1, 2, 3, 4, 6, 8, 12, 16, 24, 48"),
        ("Is 91 prime?",
         ["It is odd, so not divisible by 2.",
          "9 + 1 = 10, not a multiple of 3.",
          "Does not end in 0 or 5.",
          "Try 7: 7 \u00d7 13 = 91."],
         "No \u2014 91 = 7 \u00d7 13"),
        ("Find the highest common factor of 24 and 36.",
         ["Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24.",
          "Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36.",
          "Shared: 1, 2, 3, 4, 6, 12."],
         "HCF = 12"),
        ("Find the lowest common multiple of 6 and 8.",
         ["Multiples of 6: 6, 12, 18, 24, 30\u2026",
          "Multiples of 8: 8, 16, 24, 32\u2026",
          "First number in both lists is 24."],
         "LCM = 24"),
    ],
    mistakes=[
        ("Swapping the words \u2014 \u201c12 is a factor of 3\u201d.",
         "Factors are smaller and go <em>into</em> the number. Multiples are bigger and come <em>out of</em> it. 3 is a factor of 12; 12 is a multiple of 3."),
        ("Calling 1 a prime number.",
         "1 has only one factor \u2014 itself \u2014 so it fails the \u2018exactly two factors\u2019 test. The smallest prime is 2."),
        ("Assuming all primes are odd.",
         "2 is prime and even. It is the only even prime, because every other even number has 2 as a third factor."),
        ("Missing factors because the list was built at random.",
         "Always work in pairs from 1 upwards. It is the only method that proves you have them all."),
    ],
    sections=[
        ("The primes up to 100",
         """<p>There are 25 of them, and recognising them on sight is genuinely useful:</p>
         <p class="font-mono">2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
         71, 73, 79, 83, 89, 97</p>
         <p>Note the near-misses children get wrong most often: 51 (3 \u00d7 17), 57 (3 \u00d7 19),
         87 (3 \u00d7 29) and 91 (7 \u00d7 13) all look prime and are not.</p>"""),
        ("Prime factors and factor trees",
         """<p>Every whole number above 1 breaks down into primes in exactly one way. Split
         repeatedly until only primes remain:</p>
         <p class="font-mono">60 \u2192 6 \u00d7 10 \u2192 (2 \u00d7 3) \u00d7 (2 \u00d7 5) = 2\u00b2 \u00d7 3 \u00d7 5</p>
         <p>It does not matter which split you start with \u2014 60 = 4 \u00d7 15 gives the same
         primes. That uniqueness is called the fundamental theorem of arithmetic, and it is the
         reason HCF and LCM can be read straight off the prime factorisations.</p>"""),
        ("Where this actually gets used",
         """<p>Simplifying fractions is the big one: 36/48 cancels to 3/4 in a single step if you
         know the HCF is 12, rather than three nervous halvings. Adding fractions needs the LCM for
         a common denominator. Arranging 24 children into equal teams is a factor question. Working
         out when two buses that run every 6 and every 8 minutes next leave together is an LCM
         question.</p>"""),
    ],
    faqs=[
        ("Is 1 a factor of every number?",
         "Yes, and so is the number itself. Every number has at least those two factors \u2014 primes have only those two."),
        ("What is the difference between a factor and a divisor?",
         "Nothing, in primary maths. \u2018Divisor\u2019 also names the number you are dividing by in a calculation, which is why schools usually prefer \u2018factor\u2019."),
        ("Is 0 a multiple of every number?",
         "Technically yes, since 0 \u00d7 anything = 0, but primary lists of multiples conventionally start at the number itself."),
        ("How many prime numbers are there?",
         "Infinitely many \u2014 Euclid proved it around 300 BC. There are 25 below 100 and 168 below 1,000."),
    ],
    cta=("Practise factors, multiples and primes", "practice.html?year=6&level=medium"),
    related=["square-cube-numbers", "times-tables", "equivalent-fractions", "short-division"],
),

# ---------------------------------------------------------------- 5
dict(
    slug="square-cube-numbers", cat=CAT, nav="Square & cube numbers", read=5,
    h1="Square numbers, cube numbers and roots",
    card="The squares to 12\u00b2 and cubes to 5\u00b3 worth knowing, plus what a square root actually asks.",
    years="Years 5\u20136",
    seo="Square numbers, cube numbers and square roots explained | Math It!",
    desc="What square and cube numbers are, the ones to learn by heart, how square roots work, and why 3\u00b2 is not 6. Includes the squares to 15\u00b2 and cubes to 10\u00b3.",
    keywords="square numbers, cube numbers, square root, squared, cubed, square numbers to 144, KS2 square numbers, year 5 squares",
    intro="""<p>A square number is what you get when a whole number is multiplied by itself:
      5 \u00d7 5 = 25, so 25 is a square number. A cube number uses three copies:
      4 \u00d7 4 \u00d7 4 = 64.</p>
      <p>The names come from shapes. 25 counters make a 5-by-5 square; 64 cubes stack into a
      4-by-4-by-4 cube. That picture is worth keeping, because it explains why these numbers appear
      whenever you work with area or volume.</p>""",
    steps=[
        ("Read the notation properly",
         "<p>5\u00b2 is said \u201cfive squared\u201d and means 5 \u00d7 5. 4\u00b3 is \u201cfour cubed\u201d "
         "and means 4 \u00d7 4 \u00d7 4. The small raised number counts how many copies are multiplied, "
         "and it is called the index or power.</p>"),
        ("Learn the squares to 12\u00b2",
         "<p>1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144. They sit on the diagonal of a times "
         "tables grid, so if the tables are secure these are already half-known.</p>"),
        ("Learn the small cubes",
         "<p>1, 8, 27, 64, 125 and 1,000 for 10\u00b3. Those six cover almost everything a primary "
         "question will ask.</p>"),
        ("Square root reverses squaring",
         "<p>\u221a49 asks \u201cwhat number multiplied by itself gives 49?\u201d The answer is 7. "
         "If you know the squares, you know the roots \u2014 it is the same list read backwards.</p>"),
        ("Spot the gaps between squares",
         "<p>1, 4, 9, 16, 25\u2026 the differences are 3, 5, 7, 9 \u2014 consecutive odd numbers. "
         "A neat pattern, and a quick way to extend the list without multiplying.</p>"),
    ],
    examples=[
        ("Work out 7\u00b2 + 3\u00b3.",
         ["7\u00b2 = 7 \u00d7 7 = 49.",
          "3\u00b3 = 3 \u00d7 3 \u00d7 3 = 27.",
          "49 + 27."],
         "76"),
        ("What is \u221a81?",
         ["Ask: what number times itself makes 81?",
          "9 \u00d7 9 = 81."],
         "9"),
        ("A square patio has an area of 144 m\u00b2. How long is each side?",
         ["Area of a square = side \u00d7 side.",
          "So side = \u221a144.",
          "12 \u00d7 12 = 144."],
         "12 m"),
        ("Which is larger, 4\u00b3 or 8\u00b2?",
         ["4\u00b3 = 4 \u00d7 4 \u00d7 4 = 64.",
          "8\u00b2 = 8 \u00d7 8 = 64.",
          "They are the same."],
         "Equal \u2014 both are 64"),
    ],
    mistakes=[
        ("Reading 3\u00b2 as 3 \u00d7 2 = 6.",
         "The index counts copies of the base, it is not a multiplier. 3\u00b2 = 3 \u00d7 3 = 9."),
        ("Thinking 5\u00b3 means 5 \u00d7 3.",
         "It means three 5s multiplied: 5 \u00d7 5 \u00d7 5 = 125."),
        ("Forgetting indices come before multiplication in BIDMAS.",
         "In 2 \u00d7 3\u00b2 you square first: 2 \u00d7 9 = 18, not (2 \u00d7 3)\u00b2 = 36."),
        ("Assuming square numbers are rare, so 1 does not count.",
         "1 \u00d7 1 = 1, so 1 is a square number \u2014 and a cube number too."),
    ],
    sections=[
        ("The full reference list",
         """<p>Squares to 15\u00b2: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225.</p>
         <p>Cubes to 10\u00b3: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000.</p>
         <p>Primary expects the squares to 12\u00b2 and the cubes to 5\u00b3 at minimum. The rest are a
         bonus that pays off quickly at secondary.</p>"""),
        ("Where squares and cubes turn up",
         """<p>Area is measured in square units because you multiply two lengths; volume uses cubic
         units because you multiply three. A 6 cm square has an area of 36 cm\u00b2 and a 6 cm cube
         has a volume of 216 cm\u00b3.</p>
         <p>They also appear in Pythagoras' theorem at secondary, in standard form, and in any
         formula involving scaling: double the sides of a square and the area goes up four times,
         not two.</p>"""),
        ("Units matter",
         """<p>Writing cm\u00b2 or m\u00b3 is not decoration \u2014 it is part of the answer and marks
         are lost without it. A useful check: area answers always carry a squared unit, volume
         answers a cubed one, and perimeter or length answers a plain one.</p>"""),
    ],
    faqs=[
        ("Why is it called \u2018squared\u2019?",
         "Because the number of counters needed to build a square with that side length is exactly the number multiplied by itself. 4 \u00d7 4 counters make a 4-by-4 square."),
        ("Can a square number be negative?",
         "Not when you square a whole number \u2014 a negative times a negative is positive. So square numbers themselves are always 0 or positive."),
        ("What is the square root of 2?",
         "About 1.414. It is irrational, meaning it cannot be written exactly as a fraction or terminating decimal. Primary questions stick to perfect squares."),
        ("Is 0 a square number?",
         "Yes, 0 \u00d7 0 = 0. Most primary lists start at 1 because 0 adds nothing useful."),
    ],
    cta=("Practise squares, cubes and roots", "practice.html?year=6&level=hard"),
    related=["factors-multiples-primes", "order-of-operations", "times-tables", "powers-of-ten"],
),

]
