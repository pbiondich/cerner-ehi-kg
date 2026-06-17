# BR_REC

> Stores Bedrock recommendations

**Description:** BR_RECOMMENDATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEDROCK_IND` | DOUBLE |  |  | recommendation run by bedrock or not. |
| 3 | `CATEGORY_MEAN` | VARCHAR(50) |  |  | Meaning for the category each recommendation should appear under |
| 4 | `CLIENT_VIEW_IND` | DOUBLE |  |  | recommendation is turned on or off for the client |
| 5 | `CODE_LVL_TXT_ID` | DOUBLE | NOT NULL |  | ID for the text stored on br_long_text |
| 6 | `CURR_OVERRIDE_NOTE` | DOUBLE |  |  | Stores the note ID from the br_name_value table |
| 7 | `DESIGN_DECISION_TXT_ID` | DOUBLE | NOT NULL |  | ID for the text stored on br_long_text |
| 8 | `DETAIL_PROGRAM_NAME` | VARCHAR(50) |  |  | Name of the program that is run to return the recommendation details |
| 9 | `HIGH_IMPACT_IND` | DOUBLE | NOT NULL |  | Indicates if the recommendation is high impact or not. A value of 1 indicates a high impact recommendation. |
| 10 | `LONG_DESC` | VARCHAR(256) |  |  | Long description of the recommendation |
| 11 | `OVERRIDE_DT_TM` | DATETIME |  |  | Date/time recommendation was overridden |
| 12 | `OVERRIDE_IND` | DOUBLE |  |  | recommendation has been overridden or not |
| 13 | `OVERRIDE_MEAN` | VARCHAR(50) |  |  | Stores the override meaning |
| 14 | `OVERRIDE_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel id of the person who overrode the recommendation |
| 15 | `PROGRAM_NAME` | VARCHAR(50) |  |  | Name of the program that is run to check the recommendation |
| 16 | `RATIONALE_TXT_ID` | DOUBLE | NOT NULL |  | ID for the text stored on br_long_text |
| 17 | `RECOMMENDATION_TXT_ID` | DOUBLE | NOT NULL |  | ID for the text stored on br_long_text |
| 18 | `REC_ID` | DOUBLE | NOT NULL |  | Unique ID for the table |
| 19 | `REC_MEAN` | VARCHAR(50) |  |  | Unique meaning given to a recommendation |
| 20 | `RELEASE_DATE_TXT` | VARCHAR(50) | NOT NULL |  | Stores the date of the release in which the recommendation was released, ex. "June 2010" |
| 21 | `RELEASE_NBR_TXT` | VARCHAR(50) | NOT NULL |  | Stores the number of the release in which the recommendation was released, ex. "Administration.25" |
| 22 | `RESOLUTION_TXT_ID` | DOUBLE | NOT NULL |  | ID for the text stored on br_long_text |
| 23 | `SEQUENCE` | DOUBLE |  |  | Display sequence |
| 24 | `SHORT_DESC` | VARCHAR(100) |  |  | Short description of the recommendation |
| 25 | `SPEC_CONS_TXT_ID` | DOUBLE | NOT NULL |  | ID from the long_text table where the special considerations text is stored |
| 26 | `SUBCATEGORY_MEAN` | VARCHAR(50) |  |  | Meaning for the subcategory each recommendation should appear under |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

