# -*- coding: utf-8 -*-
"""Guides: Fractions."""

CAT = "Fractions"

GUIDES = [

# ---------------------------------------------------------------- 1
dict(
    slug="fractions-explained", cat=CAT, nav="Fractions explained", read=6,
    h1="Fractions explained from the beginning",
    card="What the two numbers mean, how to compare fractions, and the vocabulary that gets assumed.",
    years="Years 2\u20136",
    seo="Fractions explained \u2014 numerator, denominator and comparing | Math It!",
    desc="A plain-English introduction to fractions: what the numerator and denominator mean, proper and improper fractions, comparing and ordering, and why a bigger denominator means smaller pieces.",
    keywords="fractions explained, what is a fraction, numerator denominator, comparing fractions, improper fractions, KS2 fractions, year 3 fractions",
    intro="""<p>A fraction describes a part of a whole. The bottom number, the
      <strong>denominator</strong>, says how many equal pieces the whole was cut into. The top
      number, the <strong>numerator</strong>, counts how many of those pieces you have.</p>
      <p>So 3/4 means: cut into four equal parts, take three. Everything else about fractions \u2014
      adding them, comparing them, multiplying them \u2014 follows from holding onto that one
      sentence.</p>""",
    steps=[
        ("Name the parts",
         "<p>Denominator on the bottom \u2014 think \u2018down\u2019 and \u2018names the pieces\u2019. "
         "Numerator on top \u2014 it \u2018enumerates\u2019, or counts them.</p>"),
        ("Insist on equal parts",
         "<p>A cake cut into four wildly uneven slices does not give quarters. The parts must be "
         "equal in size, and this is worth labouring because it is where misconceptions start.</p>"),
        ("A bigger denominator means smaller pieces",
         "<p>1/8 is smaller than 1/4, because cutting the same cake into eight gives smaller slices "
         "than cutting it into four. This feels backwards to children and needs saying often.</p>"),
        ("Compare with the same denominator",
         "<p>If the denominators match, just compare the numerators: 5/8 &gt; 3/8. If they do not "
         "match, convert to a common denominator first.</p>"),
        ("Know the three types",
         "<p><strong>Proper</strong>: top smaller than bottom (3/4). <strong>Improper</strong>: top "
         "bigger (9/4). <strong>Mixed number</strong>: a whole and a fraction together "
         "(2\u00bc).</p>"),
    ],
    examples=[
        ("Which is bigger, 2/3 or 3/5?",
         ["Different denominators, so find a common one. 3 and 5 give 15.",
          "2/3 = 10/15 (multiply top and bottom by 5).",
          "3/5 = 9/15 (multiply top and bottom by 3).",
          "10 fifteenths beats 9 fifteenths."],
         "2/3 is bigger"),
        ("What fraction of 20 counters are red if 12 are red?",
         ["Total pieces = 20, so the denominator is 20.",
          "Red counters = 12, so the numerator is 12.",
          "12/20 simplifies: both divide by 4."],
         "3/5"),
        ("Put 1/2, 2/5 and 5/8 in order, smallest first.",
         ["Common denominator of 2, 5 and 8 is 40.",
          "1/2 = 20/40, 2/5 = 16/40, 5/8 = 25/40.",
          "Order the numerators: 16, 20, 25."],
         "2/5, 1/2, 5/8"),
    ],
    mistakes=[
        ("Thinking 1/8 is bigger than 1/4 because 8 &gt; 4.",
         "More pieces means smaller pieces. Draw two identical bars, split one into 4 and one into 8, and the point makes itself."),
        ("Comparing fractions by looking only at the numerators.",
         "2/3 and 3/5 cannot be compared until the denominators match. Convert first, always."),
        ("Accepting unequal parts as fractions.",
         "A shape split into three pieces only shows thirds if the three pieces are the same size."),
        ("Reading 3/4 as \u2018three and four\u2019.",
         "Say \u2018three quarters\u2019 or \u2018three out of four equal parts\u2019. The language carries the meaning."),
    ],
    sections=[
        ("Fractions are also divisions",
         """<p>3/4 means 3 \u00f7 4. That is not a coincidence or a separate fact \u2014 it is the same
         statement. Sharing 3 cakes between 4 people gives each person 3/4 of a cake.</p>
         <p>This dual meaning is what lets you convert any fraction to a decimal with
         <a href="short-division.html" class="link">short division</a>: 3 \u00f7 4 = 0.75.
         It is also why a fraction bar behaves like a bracket in BIDMAS.</p>"""),
        ("The fraction wall",
         """<p>A fraction wall \u2014 a stack of identical bars divided into halves, thirds,
         quarters, fifths and so on \u2014 is the single most useful fractions resource. It makes
         three things immediately visible:</p>
         <ul>
           <li>Which fractions are equivalent (1/2 lines up exactly with 2/4 and 3/6).</li>
           <li>Which fractions are bigger (2/3 extends further than 3/5).</li>
           <li>Why common denominators are needed to add (the pieces must be the same size).</li>
         </ul>"""),
        ("Where fractions go next",
         """<p>Once the basics are secure, the curriculum path is:
         <a href="equivalent-fractions.html" class="link">equivalent fractions and simplifying</a>,
         then <a href="adding-subtracting-fractions.html" class="link">adding and subtracting</a>,
         then <a href="multiplying-fractions.html" class="link">multiplying</a> and
         <a href="dividing-fractions.html" class="link">dividing</a>, with
         <a href="mixed-numbers.html" class="link">mixed numbers</a> threaded throughout.</p>
         <p>It is worth doing them in that order. Nearly every fractions difficulty at the top end
         turns out to be an equivalence problem in disguise.</p>"""),
    ],
    faqs=[
        ("What is the easiest way to explain a fraction to a child?",
         "Cut something real into equal pieces \u2014 pizza, chocolate, a strip of paper. The denominator is how many pieces you made, the numerator is how many you took."),
        ("When do children start fractions?",
         "Halves and quarters of shapes and small quantities appear in Year 1. Formal work with equivalence, addition and comparison runs from Year 3 to Year 6."),
        ("Can the numerator be bigger than the denominator?",
         "Yes \u2014 that is an improper or top-heavy fraction, like 9/4. It is perfectly valid and equals 2\u00bc."),
        ("Why do fractions feel harder than whole numbers?",
         "Because the rules differ. With whole numbers, more digits means bigger; with fractions a bigger denominator means smaller. Children have to unlearn an assumption, which is harder than learning something new."),
    ],
    cta=("Practise fractions questions", "practice.html?year=5&level=medium"),
    related=["equivalent-fractions", "adding-subtracting-fractions", "mixed-numbers", "fractions-of-amounts"],
),

# ---------------------------------------------------------------- 2
dict(
    slug="equivalent-fractions", cat=CAT, nav="Equivalent fractions", read=5,
    h1="Equivalent fractions and simplifying",
    card="Multiply or divide top and bottom by the same number \u2014 and always simplify fully.",
    years="Years 3\u20136",
    seo="Equivalent fractions and simplifying explained | Math It!",
    desc="How to find equivalent fractions, how to simplify to lowest terms using the highest common factor, and why only multiplying or dividing both parts is allowed.",
    keywords="equivalent fractions, simplifying fractions, lowest terms, cancelling fractions, highest common factor fractions, KS2 equivalent fractions, year 5 simplifying",
    intro="""<p>Two fractions are equivalent when they represent the same amount written differently.
      1/2, 2/4, 3/6 and 50/100 are all the same quantity.</p>
      <p>You move between them by multiplying or dividing <em>both</em> the numerator and the
      denominator by the same number. Going up is called finding an equivalent; going down is called
      simplifying or cancelling.</p>""",
    steps=[
        ("Multiply both parts to scale up",
         "<p>2/3 \u00d7 (4/4) = 8/12. Multiplying top and bottom by the same number is multiplying by "
         "1 in disguise, which is why the value does not change.</p>"),
        ("Divide both parts to simplify",
         "<p>8/12 \u00f7 (4/4) = 2/3. You can only divide if the number goes exactly into both.</p>"),
        ("Find the highest common factor",
         "<p>To simplify in one step, divide by the HCF of the two numbers. For 36/48, the HCF is "
         "12, giving 3/4 immediately.</p>"),
        ("Or halve repeatedly",
         "<p>If finding the HCF is hard, keep dividing by small numbers until nothing works. "
         "36/48 \u2192 18/24 \u2192 9/12 \u2192 3/4. Slower, but it always lands in the same place.</p>"),
        ("Check you have finished",
         "<p>A fraction is in its lowest terms when the only number that divides both parts is 1. "
         "If both are even, you are not finished.</p>"),
    ],
    examples=[
        ("Simplify 36/48.",
         ["Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36.",
          "Factors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48.",
          "Highest common factor is 12.",
          "36 \u00f7 12 = 3 and 48 \u00f7 12 = 4."],
         "3/4"),
        ("Write 3/5 with a denominator of 40.",
         ["5 \u00d7 8 = 40, so the scale factor is 8.",
          "Do the same to the top: 3 \u00d7 8 = 24."],
         "24/40"),
        ("Is 7/21 the same as 1/3?",
         ["Simplify 7/21: both divide by 7.",
          "7 \u00f7 7 = 1 and 21 \u00f7 7 = 3."],
         "Yes \u2014 both equal 1/3"),
        ("Simplify 150/200.",
         ["Both end in zeros, so divide by 10: 15/20.",
          "Both divide by 5: 3/4.",
          "Nothing divides 3 and 4 except 1."],
         "3/4"),
    ],
    mistakes=[
        ("Adding the same number to top and bottom.",
         "2/3 is not 3/4. Only multiplying or dividing preserves the value, because only those scale both parts proportionally."),
        ("Simplifying only partway and stopping.",
         "18/24 is correct but not simplified. If both numbers are still even, or both end in 5 or 0, keep going."),
        ("Cancelling a number that only goes into one part.",
         "To cancel by 3, the 3 must divide the numerator <em>and</em> the denominator exactly."),
        ("Thinking a scaled-up fraction is \u2018bigger\u2019.",
         "8/12 is exactly the same amount as 2/3 \u2014 more pieces, but each one smaller."),
    ],
    sections=[
        ("Why multiplying both parts is legal",
         """<p>Multiplying the numerator and denominator by 4 is the same as multiplying the whole
         fraction by 4/4, and 4/4 is just 1. Multiplying anything by 1 leaves it unchanged.</p>
         <p>Adding 4 to both parts is not multiplying by anything \u2014 it changes the ratio between
         the parts, and therefore changes the value. Saying this once, properly, prevents the most
         persistent error in the topic.</p>"""),
        ("When to simplify and when not to",
         """<p>Simplify at the end of a calculation, almost always \u2014 SATs mark schemes usually
         accept unsimplified answers, but many textbooks and all secondary teachers expect lowest
         terms.</p>
         <p>Do <em>not</em> simplify partway through adding or subtracting, when you have gone to the
         trouble of finding a common denominator. And when multiplying, simplifying before you
         multiply (cross-cancelling) makes the numbers far smaller \u2014 that is the one case where
         early simplification helps.</p>"""),
        ("Equivalence underpins everything else",
         """<p>Adding fractions needs equivalence to find a common denominator. Comparing fractions
         needs it. Converting to percentages uses it (3/4 = 75/100 = 75%). Ratio simplification is
         the same operation with different notation.</p>
         <p>If a child is struggling with fractions generally, test equivalence first. It is usually
         the gap.</p>"""),
    ],
    faqs=[
        ("What does \u2018lowest terms\u2019 mean?",
         "The fraction has been simplified as far as it can go \u2014 the only whole number dividing both the numerator and denominator is 1."),
        ("Do I have to simplify my answer in SATs?",
         "Generally no \u2014 mark schemes accept equivalent fractions unless the question says \u2018in its simplest form\u2019. But it is a good habit and it is expected at secondary."),
        ("What is cross-cancelling?",
         "Simplifying diagonally across a multiplication before multiplying, e.g. 2/3 \u00d7 9/10 \u2014 cancel the 3 and 9 to 1 and 3, and the 2 and 10 to 1 and 5, giving 3/5 directly."),
        ("How do I find the highest common factor quickly?",
         "List factor pairs of both numbers and take the largest shared one, or use prime factorisation. Repeated halving also works if finding the HCF is slow."),
    ],
    cta=("Practise equivalent fractions", "practice.html?year=5&level=medium"),
    related=["fractions-explained", "adding-subtracting-fractions", "factors-multiples-primes", "fractions-decimals-percentages"],
),

# ---------------------------------------------------------------- 3
dict(
    slug="adding-subtracting-fractions", cat=CAT, nav="Adding & subtracting fractions", read=6,
    h1="Adding and subtracting fractions",
    card="Same denominator? Easy. Different? Find a common one first \u2014 here is how.",
    years="Years 4\u20136",
    seo="Adding and subtracting fractions \u2014 common denominators explained | Math It!",
    desc="How to add and subtract fractions with the same and with different denominators, how to find the lowest common denominator, and how to handle mixed numbers.",
    keywords="adding fractions, subtracting fractions, common denominator, lowest common denominator, adding fractions different denominators, KS2 adding fractions, year 6 fractions",
    intro="""<p>You can only add fractions when the pieces are the same size. 3/8 + 2/8 = 5/8 because
      both are eighths \u2014 three eighths plus two eighths is five eighths, in exactly the way three
      apples plus two apples is five apples.</p>
      <p>When the denominators differ you must first rewrite them so they match. That is the whole
      skill; everything else is addition.</p>""",
    steps=[
        ("Check the denominators",
         "<p>Same? Go straight to step 4. Different? Carry on.</p>"),
        ("Find a common denominator",
         "<p>The lowest common multiple of the two denominators is the tidiest choice. For 4 and 6 "
         "that is 12. If you cannot see it, multiplying the two denominators always works \u2014 it "
         "just gives bigger numbers to simplify later.</p>"),
        ("Convert both fractions",
         "<p>Scale each one up using equivalent fractions. 3/4 = 9/12 (\u00d73) and 1/6 = 2/12 "
         "(\u00d72). Remember both the top and the bottom.</p>"),
        ("Add or subtract the numerators only",
         "<p>9/12 + 2/12 = 11/12. The denominator stays exactly as it is \u2014 you are counting "
         "twelfths, and the size of a twelfth has not changed.</p>"),
        ("Simplify, and convert back if needed",
         "<p>If the answer is top-heavy, turn it into a mixed number. If it simplifies, simplify "
         "it.</p>"),
    ],
    examples=[
        ("3/4 + 1/6",
         ["Denominators 4 and 6. Lowest common multiple is 12.",
          "3/4 = 9/12, 1/6 = 2/12.",
          "Add the numerators: 9 + 2 = 11.",
          "11/12 will not simplify."],
         "11/12"),
        ("5/6 \u2212 1/4",
         ["LCM of 6 and 4 is 12.",
          "5/6 = 10/12, 1/4 = 3/12.",
          "10 \u2212 3 = 7."],
         "7/12"),
        ("2/3 + 3/4",
         ["LCM of 3 and 4 is 12.",
          "2/3 = 8/12, 3/4 = 9/12.",
          "8 + 9 = 17, so 17/12 \u2014 top-heavy.",
          "17 \u00f7 12 = 1 remainder 5."],
         "1 and 5/12"),
        ("3 and 1/2 \u2212 1 and 3/4",
         ["Convert to improper: 7/2 and 7/4.",
          "Common denominator 4: 14/4 and 7/4.",
          "14 \u2212 7 = 7, so 7/4.",
          "7 \u00f7 4 = 1 remainder 3."],
         "1 and 3/4"),
    ],
    mistakes=[
        ("Adding the denominators: 1/2 + 1/3 = 2/5.",
         "The denominator names the piece size and does not change. 1/2 + 1/3 = 3/6 + 2/6 = 5/6 \u2014 and note 5/6 is bigger than either, as it must be."),
        ("Converting one fraction but not the other.",
         "Both must end up over the same denominator. Write both conversions out before adding anything."),
        ("Scaling the denominator but forgetting the numerator.",
         "Whatever you do to the bottom you must do to the top. 3/4 to twelfths is 9/12, not 3/12."),
        ("Leaving a top-heavy answer when a mixed number was asked for.",
         "17/12 is correct but may not be the requested form. Read the question."),
    ],
    sections=[
        ("Choosing a common denominator",
         """<p>Two approaches, both valid:</p>
         <ul>
           <li><strong>Lowest common multiple.</strong> For 6 and 8, the LCM is 24. Smaller numbers,
           less simplifying afterwards.</li>
           <li><strong>Multiply the denominators.</strong> 6 \u00d7 8 = 48. Always works, needs no
           thought, but produces larger numbers.</li>
         </ul>
         <p>Teach the LCM as the goal and the product as the fallback. A child who freezes trying to
         find the LCM should just multiply and simplify at the end \u2014 a correct answer by the
         long route beats a blank page.</p>"""),
        ("Mixed numbers: two routes",
         """<p>For 3\u00bd \u2212 1\u00be you can either convert both to improper fractions and
         subtract, or deal with the whole numbers and the fractions separately. The improper
         fraction route is more reliable because the separate route can require exchanging a whole
         into fractions, which is where errors creep in.</p>
         <p>For addition, the separate route is usually fine and faster: 2\u2153 + 1\u00bc = 3 +
         (4/12 + 3/12) = 3 and 7/12.</p>"""),
        ("A sanity check that catches most errors",
         """<p>Adding two positive fractions must give something bigger than both. Subtracting must
         give something smaller than the first. If 1/2 + 1/3 came out as 2/5, that is smaller than
         1/2 \u2014 so it is wrong, without needing to find the error.</p>
         <p>This check takes a second and catches the denominator-adding mistake every single
         time.</p>"""),
    ],
    faqs=[
        ("Why can't you just add the denominators?",
         "Because the denominator says what size the pieces are, not how many there are. Adding half a pizza and a third of a pizza gives more than half a pizza \u2014 2/5 would be less."),
        ("Do the denominators have to be the lowest common multiple?",
         "No, any common denominator works. The LCM just keeps the numbers small."),
        ("How do I subtract when the first fraction is smaller?",
         "With mixed numbers, exchange one whole into fractions first \u2014 or convert both to improper fractions, which avoids the issue entirely."),
        ("When is this taught?",
         "Adding fractions with the same denominator is Year 3 to 4. Different denominators, where one is a multiple of the other, is Year 5. Any denominators is Year 6."),
    ],
    cta=("Practise adding and subtracting fractions", "practice.html?year=6&level=medium"),
    related=["equivalent-fractions", "mixed-numbers", "multiplying-fractions", "factors-multiples-primes"],
),

# ---------------------------------------------------------------- 4
dict(
    slug="multiplying-fractions", cat=CAT, nav="Multiplying fractions", read=5,
    h1="Multiplying fractions",
    card="Tops times tops, bottoms times bottoms \u2014 the easiest fraction operation, oddly.",
    years="Years 5\u20136",
    seo="Multiplying fractions explained \u2014 with worked examples | Math It!",
    desc="How to multiply fractions: multiply the numerators, multiply the denominators, simplify. Includes multiplying by whole numbers, mixed numbers, and why the answer gets smaller.",
    keywords="multiplying fractions, multiply fractions, fraction times fraction, fraction of a number, multiplying mixed numbers, KS2 multiplying fractions, year 6",
    intro="""<p>Multiplying fractions is the easiest of the four operations, which surprises everybody.
      There is no common denominator to find. You multiply the numerators together, multiply the
      denominators together, and simplify.</p>
      <p>2/3 \u00d7 3/5 = 6/15 = 2/5. That is the whole method.</p>""",
    steps=[
        ("Multiply the numerators",
         "<p>The two top numbers, straight across.</p>"),
        ("Multiply the denominators",
         "<p>The two bottom numbers, straight across.</p>"),
        ("Simplify the result",
         "<p>6/15 both divide by 3, giving 2/5.</p>"),
        ("Turn whole numbers into fractions first",
         "<p>5 is 5/1. So 5 \u00d7 2/3 = 5/1 \u00d7 2/3 = 10/3 = 3\u2153.</p>"),
        ("Convert mixed numbers before multiplying",
         "<p>1\u00bd \u00d7 2\u2153 must become 3/2 \u00d7 7/3. Never multiply the whole parts and the "
         "fraction parts separately \u2014 that does not work.</p>"),
        ("Cancel early if you can",
         "<p>In 2/3 \u00d7 9/10, cancel the 3 into the 9 and the 2 into the 10 before multiplying: "
         "1/1 \u00d7 3/5 = 3/5. Much smaller numbers, same answer.</p>"),
    ],
    examples=[
        ("2/3 \u00d7 3/5",
         ["Numerators: 2 \u00d7 3 = 6.",
          "Denominators: 3 \u00d7 5 = 15.",
          "6/15 \u2014 both divide by 3."],
         "2/5"),
        ("3/4 of 20",
         ["\u2018Of\u2019 means multiply: 3/4 \u00d7 20/1.",
          "Numerators: 3 \u00d7 20 = 60. Denominators: 4 \u00d7 1 = 4.",
          "60/4 = 15. (Or: 20 \u00f7 4 = 5, then \u00d7 3.)"],
         "15"),
        ("1\u00bd \u00d7 2\u2153",
         ["Convert: 1\u00bd = 3/2 and 2\u2153 = 7/3.",
          "3 \u00d7 7 = 21, and 2 \u00d7 3 = 6.",
          "21/6 simplifies by 3 to 7/2.",
          "7 \u00f7 2 = 3 remainder 1."],
         "3\u00bd"),
        ("2/3 \u00d7 9/10 using cancelling",
         ["3 goes into 9 three times: the 3 becomes 1, the 9 becomes 3.",
          "2 goes into 10 five times: the 2 becomes 1, the 10 becomes 5.",
          "Now 1/1 \u00d7 3/5."],
         "3/5"),
    ],
    mistakes=[
        ("Finding a common denominator first.",
         "That is for adding and subtracting. Multiplication needs no common denominator at all \u2014 going looking for one wastes time and introduces errors."),
        ("Multiplying mixed numbers part by part: 1\u00bd \u00d7 2\u2153 = 2 and \u215b.",
         "Convert both to improper fractions first. The parts do not multiply independently."),
        ("Expecting the answer to be bigger.",
         "Multiplying by a fraction less than 1 makes things smaller. 3/4 of 20 is 15, less than 20. That is correct."),
        ("Forgetting to simplify at the end.",
         "6/15 is right but not finished. Check whether any number divides both parts."),
    ],
    sections=[
        ("Why multiplying can make things smaller",
         """<p>Children spend years learning that multiplication makes numbers bigger, so 3/4 of 20
         being 15 feels wrong. The fix is the word \u201cof\u201d: multiplying by 3/4 means taking
         three quarters <em>of</em> something, which is obviously less than all of it.</p>
         <p>Three cases worth stating explicitly: multiplying by a fraction less than 1 makes it
         smaller, multiplying by exactly 1 leaves it the same, multiplying by a mixed number greater
         than 1 makes it bigger.</p>"""),
        ("\u2018Of\u2019 means multiply",
         """<p>\u201cWhat is 2/5 of 35?\u201d is 2/5 \u00d7 35. Mentally it is usually easier to divide
         first: 35 \u00f7 5 = 7, then 7 \u00d7 2 = 14. Same calculation, smaller numbers.</p>
         <p>That shortcut is covered fully in
         <a href="fractions-of-amounts.html" class="link">fractions of amounts</a>, and it is the
         route most children should use for this question type.</p>"""),
        ("Cross-cancelling saves real time",
         """<p>Multiplying 8/15 \u00d7 5/12 straight across gives 40/180, which then needs simplifying
         by 20. Cancelling first \u2014 5 into 15 and 4 into 8 and 12 \u2014 gives 2/9 directly.</p>
         <p>The arithmetic is smaller, the simplification is already done, and there is less to get
         wrong. It is worth teaching as soon as multiplication itself is secure.</p>"""),
    ],
    faqs=[
        ("Do you need a common denominator to multiply fractions?",
         "No. That requirement belongs to addition and subtraction only. Multiply straight across."),
        ("How do you multiply a fraction by a whole number?",
         "Write the whole number over 1. 5 \u00d7 2/3 becomes 5/1 \u00d7 2/3 = 10/3. Or just multiply the numerator by the whole number."),
        ("What does \u2018of\u2019 mean in fraction questions?",
         "Multiply. \u20183/4 of 20\u2019 is 3/4 \u00d7 20."),
        ("Why does the answer get smaller?",
         "Because you are taking a part of something. Three quarters of a quantity is less than the whole quantity."),
    ],
    cta=("Practise multiplying fractions", "practice.html?year=6&level=medium"),
    related=["dividing-fractions", "fractions-of-amounts", "mixed-numbers", "equivalent-fractions"],
),

# ---------------------------------------------------------------- 5
dict(
    slug="dividing-fractions", cat=CAT, nav="Dividing fractions", read=6,
    h1="Dividing fractions: keep, change, flip",
    card="Turn the second fraction upside down and multiply \u2014 and understand why that works.",
    years="Year 6",
    seo="Dividing fractions explained \u2014 keep, change, flip | Math It!",
    desc="How to divide fractions using the reciprocal: keep the first, change the sign, flip the second. Includes dividing by whole numbers and why the answer often gets bigger.",
    keywords="dividing fractions, keep change flip, reciprocal fractions, divide fractions by whole number, fraction division, year 6 dividing fractions, KS2",
    intro="""<p>Dividing by a fraction is the same as multiplying by its reciprocal \u2014 the fraction
      turned upside down. Schools teach this as <strong>keep, change, flip</strong>: keep the first
      fraction, change \u00f7 into \u00d7, flip the second.</p>
      <p>It is a reliable rule, and it is worth spending five minutes on why it is true, because the
      \u201cwhy\u201d is what stops children flipping the wrong fraction.</p>""",
    steps=[
        ("Keep the first fraction exactly as it is",
         "<p>Do not touch it. Only the second fraction changes.</p>"),
        ("Change the division sign to multiplication",
         "<p>\u00f7 becomes \u00d7.</p>"),
        ("Flip the second fraction",
         "<p>Swap its numerator and denominator. 2/5 becomes 5/2. This is its reciprocal.</p>"),
        ("Multiply as normal",
         "<p>Tops across, bottoms across, then simplify.</p>"),
        ("Whole numbers get a denominator of 1",
         "<p>Dividing by 4 means dividing by 4/1, which flips to 1/4. So \u00f7 4 is the same as "
         "\u00d7 1/4 \u2014 which is just halving twice.</p>"),
        ("Convert mixed numbers first",
         "<p>2\u00bd \u00f7 1\u00bc must become 5/2 \u00f7 5/4 before anything else happens.</p>"),
    ],
    examples=[
        ("3/4 \u00f7 2/5",
         ["Keep 3/4.",
          "Change \u00f7 to \u00d7.",
          "Flip 2/5 to 5/2.",
          "3 \u00d7 5 = 15 and 4 \u00d7 2 = 8, so 15/8.",
          "15 \u00f7 8 = 1 remainder 7."],
         "1 and 7/8"),
        ("2/3 \u00f7 4",
         ["Write 4 as 4/1.",
          "Keep 2/3, change to \u00d7, flip to 1/4.",
          "2 \u00d7 1 = 2 and 3 \u00d7 4 = 12.",
          "2/12 simplifies by 2."],
         "1/6"),
        ("How many quarters are there in 3?",
         ["This is 3 \u00f7 1/4.",
          "Keep 3/1, change to \u00d7, flip 1/4 to 4/1.",
          "3 \u00d7 4 = 12 and 1 \u00d7 1 = 1."],
         "12"),
        ("2\u00bd \u00f7 1\u00bc",
         ["Convert: 5/2 \u00f7 5/4.",
          "Keep 5/2, change to \u00d7, flip to 4/5.",
          "5 \u00d7 4 = 20 and 2 \u00d7 5 = 10.",
          "20/10."],
         "2"),
    ],
    mistakes=[
        ("Flipping the first fraction instead of the second.",
         "Only the divisor \u2014 the one after the \u00f7 sign \u2014 is flipped. Say \u2018keep, change, flip\u2019 in that order, touching each part as you say it."),
        ("Flipping both fractions.",
         "That gives the reciprocal of the answer. One flip only."),
        ("Changing the sign but forgetting to flip, or flipping but leaving \u00f7.",
         "They are a pair. Write the new calculation out in full before computing anything."),
        ("Expecting the answer to be smaller.",
         "Dividing by a fraction less than 1 makes the answer bigger. 3 \u00f7 1/4 = 12, and that is correct \u2014 there are twelve quarters in three."),
    ],
    sections=[
        ("Why flipping works",
         """<p>Division asks \u201chow many of these fit into that?\u201d. 3 \u00f7 1/4 asks how many
         quarters fit into 3. Each whole contains 4 quarters, so three wholes contain 12 \u2014 which
         is exactly 3 \u00d7 4.</p>
         <p>More formally: dividing by 1/4 and multiplying by 4 have the same effect because 1/4 and
         4 are reciprocals, and multiplying by a number then by its reciprocal gets you back where
         you started. The flip is not a trick; it is the definition of division restated.</p>"""),
        ("Dividing by a whole number",
         """<p>2/3 \u00f7 4 can be done two ways. Keep-change-flip gives 2/3 \u00d7 1/4 = 2/12 = 1/6.
         Alternatively, just multiply the denominator by 4: 2/(3\u00d74) = 2/12. Same answer, and the
         second is quicker once children trust it.</p>
         <p>Picture it: two thirds shared between four people. Each third splits into four, so the
         whole is now in twelfths, and each person gets two of them.</p>"""),
        ("Checking with multiplication",
         """<p>If 3/4 \u00f7 2/5 = 15/8, then 15/8 \u00d7 2/5 should return 3/4. Multiply it out:
         30/40 = 3/4. It does.</p>
         <p>That check is cheap and it is the only thing that reliably catches a wrong-fraction
         flip, because the arithmetic of a wrongly flipped division still looks tidy.</p>"""),
    ],
    faqs=[
        ("What is a reciprocal?",
         "The fraction turned upside down. The reciprocal of 3/4 is 4/3; the reciprocal of 5 is 1/5. A number multiplied by its reciprocal always gives 1."),
        ("Why does dividing by a fraction make the answer bigger?",
         "Because you are asking how many small pieces fit into the amount, and small pieces fit many times. 3 \u00f7 1/4 = 12."),
        ("Can I divide fractions without flipping?",
         "Yes \u2014 with a common denominator you can divide the numerators: 3/4 \u00f7 2/4 = 3 \u00f7 2 = 3/2. It works but is rarely taught in UK schools."),
        ("When do children learn to divide fractions?",
         "Year 6 covers dividing a proper fraction by a whole number. Dividing a fraction by a fraction is normally secondary, though it appears in extension work."),
    ],
    cta=("Practise dividing fractions", "practice.html?year=6&level=hard"),
    related=["multiplying-fractions", "mixed-numbers", "fractions-explained", "short-division"],
),

# ---------------------------------------------------------------- 6
dict(
    slug="mixed-numbers", cat=CAT, nav="Mixed numbers", read=5,
    h1="Mixed numbers and improper fractions",
    card="Convert either way in one step, and know which form a question actually wants.",
    years="Years 4\u20136",
    seo="Mixed numbers and improper fractions \u2014 converting both ways | Math It!",
    desc="How to convert a mixed number to an improper fraction and back, when to use each form, and how to add and subtract with mixed numbers.",
    keywords="mixed numbers, improper fractions, converting mixed numbers, top heavy fractions, mixed number to improper, KS2 mixed numbers, year 5",
    intro="""<p>A <strong>mixed number</strong> is a whole number next to a fraction: 2\u00bc. An
      <strong>improper fraction</strong> (or top-heavy fraction) puts the whole amount entirely in
      fraction form: 9/4. They are the same quantity.</p>
      <p>Mixed numbers are easier to picture; improper fractions are easier to calculate with. Being
      able to switch instantly is what matters.</p>""",
    steps=[
        ("Mixed to improper: multiply, add, keep",
         "<p>Multiply the whole number by the denominator, add the numerator, and keep the same "
         "denominator. 2\u00bc \u2192 2 \u00d7 4 = 8, + 1 = 9, so 9/4.</p>"),
        ("Improper to mixed: divide",
         "<p>Divide the numerator by the denominator. The quotient is the whole number and the "
         "remainder becomes the new numerator. 17/5 \u2192 17 \u00f7 5 = 3 remainder 2, so "
         "3 and 2/5.</p>"),
        ("Always simplify the fraction part",
         "<p>14/4 \u2192 3 remainder 2 \u2192 3 and 2/4 \u2192 3\u00bd.</p>"),
        ("Convert before multiplying or dividing",
         "<p>Mixed numbers cannot be multiplied part by part. Turn them into improper fractions "
         "first, every time.</p>"),
        ("Choose the form the question asks for",
         "<p>\u201cGive your answer as a mixed number\u201d means convert back at the end. If the "
         "question does not say, either is normally accepted at primary.</p>"),
    ],
    examples=[
        ("Convert 3 and 2/5 to an improper fraction.",
         ["3 \u00d7 5 = 15.",
          "15 + 2 = 17.",
          "Denominator stays 5."],
         "17/5"),
        ("Convert 23/6 to a mixed number.",
         ["23 \u00f7 6 = 3 remainder 5.",
          "Whole part 3, remainder 5 over the original 6."],
         "3 and 5/6"),
        ("Convert 14/4 to a mixed number in simplest form.",
         ["14 \u00f7 4 = 3 remainder 2.",
          "3 and 2/4.",
          "2/4 simplifies to 1/2."],
         "3\u00bd"),
        ("1\u00bc + 2\u2154",
         ["Whole numbers: 1 + 2 = 3.",
          "Fractions: 1/4 + 2/3 \u2192 3/12 + 8/12 = 11/12.",
          "Combine."],
         "3 and 11/12"),
    ],
    mistakes=[
        ("Adding instead of multiplying: 2\u00bc \u2192 (2 + 4 + 1)/4.",
         "The whole number must be multiplied by the denominator first. Two wholes are eight quarters, not two."),
        ("Keeping the remainder over the wrong number.",
         "The remainder always sits over the original denominator. 17/5 gives 3 and 2/<strong>5</strong>."),
        ("Multiplying mixed numbers without converting.",
         "1\u00bd \u00d7 2\u00bd is not 2 and \u00bc. Convert to 3/2 \u00d7 5/2 = 15/4 = 3\u00be."),
        ("Leaving 3 and 2/4 as the final answer.",
         "The fraction part must be simplified too. 3 and 2/4 is 3\u00bd."),
    ],
    sections=[
        ("Which form when",
         """<p>Use <strong>mixed numbers</strong> when you want to see the size of something at a
         glance, when measuring, and when a question asks for them. 3\u00be is instantly meaningful;
         15/4 is not.</p>
         <p>Use <strong>improper fractions</strong> for every calculation except simple addition of
         the whole parts. All multiplication and division of mixed numbers must go through improper
         form, and subtraction usually should too.</p>"""),
        ("Subtracting mixed numbers",
         """<p>3\u00bc \u2212 1\u00be fails if you subtract parts separately, because \u00bc is less
         than \u00be. Two options:</p>
         <ul>
           <li><strong>Convert to improper:</strong> 13/4 \u2212 7/4 = 6/4 = 1\u00bd. Clean, and it
           never fails.</li>
           <li><strong>Exchange a whole:</strong> 3\u00bc becomes 2 and 5/4, then 2 and 5/4 \u2212 1
           and 3/4 = 1 and 2/4 = 1\u00bd.</li>
         </ul>
         <p>The improper route is the one to default to.</p>"""),
        ("Reading them aloud",
         """<p>2\u00bc is \u201ctwo and a quarter\u201d \u2014 the \u201cand\u201d matters, because
         it signals addition. 2\u00bc genuinely means 2 + \u00bc. Children who hear \u201ctwo
         quarter\u201d sometimes think the 2 multiplies the fraction, which is how
         1\u00bd \u00d7 2\u00bd errors begin.</p>"""),
    ],
    faqs=[
        ("What is a top-heavy fraction?",
         "Another name for an improper fraction \u2014 one where the numerator is larger than the denominator, like 9/4."),
        ("Is an improper fraction wrong?",
         "Not at all. It is a perfectly valid way to write a number and is usually easier to calculate with. \u2018Improper\u2019 is just a label."),
        ("Which form should I give as my answer?",
         "Whatever the question asks for. If it does not specify, primary mark schemes normally accept either, though a simplified mixed number is the conventional choice."),
        ("How do I convert a mixed number with a big whole part?",
         "The same way. 12 and 3/5 is (12 \u00d7 5) + 3 = 63, so 63/5."),
    ],
    cta=("Practise mixed numbers", "practice.html?year=6&level=medium"),
    related=["adding-subtracting-fractions", "multiplying-fractions", "equivalent-fractions", "short-division"],
),

# ---------------------------------------------------------------- 7
dict(
    slug="fractions-of-amounts", cat=CAT, nav="Fractions of amounts", read=5,
    h1="Finding a fraction of an amount",
    card="Divide by the bottom, multiply by the top \u2014 and work out the reverse too.",
    years="Years 3\u20136",
    seo="Fractions of amounts \u2014 divide by the bottom, times by the top | Math It!",
    desc="How to find a fraction of a quantity: divide by the denominator, multiply by the numerator. Includes reverse problems where you know the part and need the whole.",
    keywords="fractions of amounts, fraction of a number, three quarters of, divide by the bottom times by the top, reverse fraction problems, KS2 fractions of amounts",
    intro="""<p>\u201cWhat is 3/5 of 45?\u201d is the most common fraction question in primary maths,
      and it has a two-step method that always works: <strong>divide by the bottom, multiply by the
      top</strong>.</p>
      <p>45 \u00f7 5 = 9, then 9 \u00d7 3 = 27. Dividing first keeps the numbers small, which is why
      this order is better than multiplying first.</p>""",
    steps=[
        ("Divide by the denominator",
         "<p>This tells you the size of one part. 45 \u00f7 5 = 9, so one fifth of 45 is 9.</p>"),
        ("Multiply by the numerator",
         "<p>This counts how many parts you want. 9 \u00d7 3 = 27, so three fifths of 45 is 27.</p>"),
        ("Check it is sensible",
         "<p>3/5 is a bit more than half, so the answer should be a bit more than 22.5. 27 fits.</p>"),
        ("For the reverse, divide by the numerator first",
         "<p>If 3/5 of a number is 27, then one fifth is 27 \u00f7 3 = 9, and the whole is "
         "9 \u00d7 5 = 45. Same two steps, opposite order.</p>"),
        ("Use the bar model when it is confusing",
         "<p>Draw a bar, split it into denominator-many equal boxes, write the total above. Shade "
         "numerator-many boxes. The picture answers both directions.</p>"),
    ],
    examples=[
        ("Find 3/8 of 64.",
         ["Divide by the bottom: 64 \u00f7 8 = 8.",
          "Multiply by the top: 8 \u00d7 3 = 24."],
         "24"),
        ("Find 2/3 of \u00a345.",
         ["45 \u00f7 3 = 15.",
          "15 \u00d7 2 = 30."],
         "\u00a330"),
        ("5/6 of a number is 40. What is the number?",
         ["Reverse problem \u2014 divide by the numerator first.",
          "One sixth is 40 \u00f7 5 = 8.",
          "The whole is 8 \u00d7 6."],
         "48"),
        ("A jacket costs \u00a380 and is reduced by 1/4. What do you pay?",
         ["1/4 of 80 = 80 \u00f7 4 = 20.",
          "That is the discount, not the price.",
          "80 \u2212 20 = 60. (Or: you pay 3/4, and 20 \u00d7 3 = 60.)"],
         "\u00a360"),
    ],
    mistakes=[
        ("Multiplying by the denominator and dividing by the numerator.",
         "Divide by the <em>bottom</em>, multiply by the <em>top</em>. Say it as a rhyme every time until it sticks."),
        ("Answering with the discount instead of the price.",
         "Re-read the question. \u2018Reduced by 1/4\u2019 asks what you pay \u2014 the remaining 3/4."),
        ("Giving a decimal when the context needs a whole number.",
         "2/3 of 10 children is 6.67 \u2014 which means the question is wrong, or you have misread it. Quantities of people must come out whole."),
        ("Dropping the units.",
         "\u00a330 is not 30. In money and measures questions the unit is part of the answer."),
    ],
    sections=[
        ("Why divide first",
         """<p>3/5 of 45 can be done as (3 \u00d7 45) \u00f7 5 = 135 \u00f7 5 = 27, or as
         (45 \u00f7 5) \u00d7 3 = 9 \u00d7 3 = 27. Identical answers.</p>
         <p>Dividing first keeps the numbers small and usually turns the question into one you can
         do mentally. Multiplying first produces 135, which most children then have to write down.
         Same method, half the effort.</p>"""),
        ("Reverse problems",
         """<p>\u201c2/7 of a number is 18\u201d is a question type that appears in every SATs
         reasoning paper, and it catches children who have only drilled the forward direction.</p>
         <p>The logic is identical, reversed: if two sevenths is 18, one seventh is 9, and seven
         sevenths is 63. A bar model with seven boxes, two of them labelled 18 between them, makes
         it obvious.</p>"""),
        ("The link to percentages",
         """<p>Percentages are just fractions with a denominator of 100, so the same method applies.
         25% of 80 is 1/4 of 80 is 20. 60% of 45 is 3/5 of 45 is 27.</p>
         <p>Converting an awkward percentage into a friendly fraction is often the fastest route
         \u2014 see <a href="percentages-of-amounts.html" class="link">percentages of amounts</a> for
         the full set.</p>"""),
    ],
    faqs=[
        ("What is the rule for finding a fraction of an amount?",
         "Divide by the denominator, then multiply by the numerator. \u2018Divide by the bottom, times by the top.\u2019"),
        ("How do I find the whole when I know a fraction of it?",
         "Reverse the steps: divide by the numerator to find one part, then multiply by the denominator."),
        ("Does it matter whether I divide or multiply first?",
         "Not to the answer. Dividing first keeps the numbers smaller and is usually easier mentally."),
        ("How is this different from multiplying fractions?",
         "It is the same operation \u2014 \u2018of\u2019 means multiply. This method is just the efficient way to do it when one of the numbers is a whole."),
    ],
    cta=("Practise fractions of amounts", "practice.html?year=5&level=medium"),
    related=["multiplying-fractions", "percentages-of-amounts", "fractions-explained", "equivalent-fractions"],
),

]
