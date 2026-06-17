# MLTM_DRC_PREMISE

> This table is used to store the standard Dose Range Checking contest as provided by Multum

**Description:** Multum Dose Range Checking Standard Premise Content  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 61

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_HIGH_NBR` | DOUBLE | NOT NULL |  | The high age value for a given premise |
| 2 | `AGE_LOW_NBR` | DOUBLE | NOT NULL |  | The low age value for a given premise |
| 3 | `AGE_OPERATOR_TXT` | VARCHAR(25) | NOT NULL |  | Textual string representing the operand to be used for age ranges. |
| 4 | `AGE_UNIT_CKI` | VARCHAR(50) | NOT NULL |  | The corresponding CKI value for a given age unit. |
| 5 | `AGE_UNIT_DISP` | VARCHAR(40) | NOT NULL |  | The display value for a given age unit |
| 6 | `COMMENT_TXT` | VARCHAR(255) |  |  | text to display to the user if an order was placed with a dose outside of this particular dose. |
| 7 | `CONDITION1_DESC` | VARCHAR(50) |  |  | The Multum description for the condition. First of possibly 2 conditions. |
| 8 | `CONDITION1_ID` | DOUBLE | NOT NULL |  | The internal Multum identifier for the given condition. First of possible 2. |
| 9 | `CONDITION2_DESC` | VARCHAR(50) |  |  | The Multum description for the condition. Second of possibly 2 conditions. |
| 10 | `CONDITION2_ID` | DOUBLE | NOT NULL |  | The internal Multum identifier for the given condition. Second of possible 2. |
| 11 | `CONDITION_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Stores a reference to a concept_cki which will be loaded to the DRC_PREMISE table. |
| 12 | `CORRECTED_GEST_AGE_CKI` | VARCHAR(50) | NOT NULL |  | The corresponding CKI value for a given gestational age unit |
| 13 | `CORRECTED_GEST_AGE_HIGH_NBR` | DOUBLE | NOT NULL |  | The high gestational age value for a given premise |
| 14 | `CORRECTED_GEST_AGE_LOW_NBR` | DOUBLE | NOT NULL |  | The low gestational age value for a given premise |
| 15 | `CORRECTED_GEST_AGE_OPER_TXT` | VARCHAR(25) | NOT NULL |  | Textual string representing the operand to be used for gestational age ranges. |
| 16 | `CORRECTED_GEST_AGE_UNIT_DISP` | VARCHAR(40) | NOT NULL |  | The display value for a given gestational age unit |
| 17 | `CORRECTED_GEST_AGE_UNIT_ID` | DOUBLE | NOT NULL |  | The internal Multum identifier for a given gestational age unit |
| 18 | `DOSE_RANGE_CHECK_ID` | DOUBLE | NOT NULL |  | The dose_range_check_id from the dose_range_check table, if one exists for the given grouper_id. |
| 19 | `DOSE_RANGE_TYPE` | VARCHAR(100) | NOT NULL |  | Textual string representing the dose range type flag for dose ranges |
| 20 | `DOSE_RANGE_TYPE_ID` | DOUBLE | NOT NULL |  | The internal Multum identifier for a given dose range type |
| 21 | `DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | Code value corresponding to dose_unit_cki on code set 54 |
| 22 | `DOSE_UNIT_CKI` | VARCHAR(50) | NOT NULL |  | The corresponding CKI value for a given dose unit |
| 23 | `DOSE_UNIT_DISP` | VARCHAR(40) | NOT NULL |  | The display value for a given dose unit |
| 24 | `DOSE_UNIT_ID` | DOUBLE | NOT NULL |  | The internal Multum identifier for a given dose unit |
| 25 | `DRC_CKI` | VARCHAR(100) | NOT NULL |  | Multum created unique identifier for table. |
| 26 | `DRC_DOSE_RANGE_ID` | DOUBLE | NOT NULL |  | The lowest level - dose units |
| 27 | `DRC_IDENTIFIER` | VARCHAR(45) | NOT NULL |  | unique identifier for a given dose range from Multum. combination of ! . both fields are from external database. |
| 28 | `DRC_PREMISE_ID` | DOUBLE | NOT NULL |  | The drc_premise_id from the drc_premise table for a given Multum case id, if one exists. |
| 29 | `GENDER_FLAG` | DOUBLE | NOT NULL |  | 0 - no value 1 - Male 2 - Female |
| 30 | `GROUPER_ID` | DOUBLE | NOT NULL |  | the drc grouping number for the list of similar mmdc and cnum numbers |
| 31 | `GROUPER_NAME` | VARCHAR(100) | NOT NULL |  | a textual description of the rule to allow easier viewing and building of drc functionality. |
| 32 | `HIGH_DOSE_VALUE` | DOUBLE | NOT NULL |  | The high dose value for a given dose range |
| 33 | `LIVER_DESC` | VARCHAR(50) | NOT NULL |  | The Multum description for the liver condition |
| 34 | `LOW_DOSE_VALUE` | DOUBLE | NOT NULL |  | The low dose value for a given dose range |
| 35 | `MAX_DOSE_AMT` | DOUBLE | NOT NULL |  | Foor dose range checking. The maximum safe dose for a given medication. |
| 36 | `MAX_DOSE_UNIT_CKI` | VARCHAR(99) | NOT NULL |  | The CKI for the unit of measure for maximum dose. |
| 37 | `MAX_DOSE_UNIT_DISP` | VARCHAR(40) |  |  | The display value for the unit of measure for maximum dose. |
| 38 | `MULTUM_CASE_ID` | DOUBLE | NOT NULL |  | the actual identifier for a premise from Multum. |
| 39 | `PARENT_PREMISE_ID` | DOUBLE | NOT NULL |  | The parent_premise_id from the DRC_PREMISE table |
| 40 | `PEDS_IND` | DOUBLE | NOT NULL |  | Flag to determine if row is specific to Pediatric content. |
| 41 | `RENAL_CONDITION_TXT` | VARCHAR(40) | NOT NULL |  | Multum textual description for a given renal condition |
| 42 | `RENAL_HIGH_VALUE` | DOUBLE | NOT NULL |  | The high renal value for a given premise |
| 43 | `RENAL_LOW_VALUE` | DOUBLE | NOT NULL |  | The low renal value for a given premise |
| 44 | `RENAL_OPERATOR_TXT` | VARCHAR(25) | NOT NULL |  | Textual string representing the operand to be used for renal ranges. |
| 45 | `RENAL_UNIT_CKI` | VARCHAR(50) | NOT NULL |  | The corresponding CKI value for a given renal unit |
| 46 | `RENAL_UNIT_DISP` | VARCHAR(40) | NOT NULL |  | The display value for a given renal unit |
| 47 | `RENAL_UNIT_ID` | DOUBLE | NOT NULL |  | The internal Multum identifier for a given renal unit |
| 48 | `ROUTE_DISP` | VARCHAR(40) | NOT NULL |  | The display value for a given route |
| 49 | `ROUTE_ID` | DOUBLE | NOT NULL |  | The internal Multum identifier for a given route. |
| 50 | `SMOKER_FLAG` | DOUBLE | NOT NULL |  | 0 - no value 1 - yes 2 - no |
| 51 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 52 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 53 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 54 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 55 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 56 | `WEIGHT_HIGH_VALUE` | DOUBLE | NOT NULL |  | The high weight value for a given premise |
| 57 | `WEIGHT_LOW_VALUE` | DOUBLE | NOT NULL |  | The low weight value for a given premise |
| 58 | `WEIGHT_OPERATOR_TXT` | VARCHAR(25) | NOT NULL |  | Textual string representing the operand to be used for weight ranges. |
| 59 | `WEIGHT_UNIT_CKI` | VARCHAR(50) | NOT NULL |  | The corresponding CKI value for a given weight unit |
| 60 | `WEIGHT_UNIT_DISP` | VARCHAR(40) | NOT NULL |  | The display value for a given weight unit |
| 61 | `WEIGHT_UNIT_ID` | DOUBLE | NOT NULL |  | The internal Multum identifier for a given weight unit |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

