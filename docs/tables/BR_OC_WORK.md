# BR_OC_WORK

> legacy orderables

**Description:** BEDROCK OC WORK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE` | VARCHAR(40) |  |  | The activity subtype associated to the order catalog item |
| 2 | `ACTIVITY_TYPE` | VARCHAR(40) |  |  | The activity type associated to the order catalog item |
| 3 | `ALIAS1` | VARCHAR(50) |  |  | Alias associated to order catalog item. |
| 4 | `ALIAS2` | VARCHAR(50) |  |  | Alias associated to order catalog item. |
| 5 | `ALIAS3` | VARCHAR(50) |  |  | Alias associated to order catalog item. |
| 6 | `ALIAS4` | VARCHAR(50) |  |  | Alias associated to order catalog item. |
| 7 | `ALIAS5` | VARCHAR(50) |  |  | Alias associated to order catalog item. |
| 8 | `BILL_ONLY_IND` | DOUBLE |  |  | Defined as 1 order catalog item is bill only. |
| 9 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 10 | `CARESET_IND` | DOUBLE |  |  | Defined as 1 order catalog item is a careset. |
| 11 | `CATALOG_TYPE` | VARCHAR(40) |  |  | The catalog type associated to the order catalog item |
| 12 | `COMMIT_IND` | DOUBLE | NOT NULL |  | Commit Indicator |
| 13 | `DEPT_NAME` | VARCHAR(100) |  |  | Department name for the order catalog item. |
| 14 | `DUP_CHECK_SEQ` | DOUBLE |  |  | The duplicate check sequence |
| 15 | `EXACT_HIT_ACTION_CD` | DOUBLE | NOT NULL |  | The duplicate check exact action |
| 16 | `FACILITY` | VARCHAR(50) |  |  | Used to define individual facility data. |
| 17 | `HISTORY_IND` | DOUBLE |  |  | Defined as 1 the history indicator for radiology has been defined. |
| 18 | `LOINC_CODE` | VARCHAR(10) |  |  | Loinc code associated to the order catalog item |
| 19 | `LONG_DESC` | VARCHAR(100) |  |  | Long description for the order catalog item |
| 20 | `MATCH_IND` | DOUBLE |  |  | indicates if a match has been made for that orderable |
| 21 | `MATCH_ORDERABLE_CD` | DOUBLE | NOT NULL |  | HNAM order catalog item the legacy order catalog item was matched to |
| 22 | `MATCH_VALUE` | VARCHAR(100) |  |  | The value that triggered the automated match. |
| 23 | `MIN_AHEAD` | DOUBLE |  |  | Duplicate checking minutes ahead |
| 24 | `MIN_AHEAD_ACTION_CD` | DOUBLE | NOT NULL |  | Duplicate checking minutes ahead action |
| 25 | `MIN_BEHIND` | DOUBLE |  |  | Duplicate checking minutes behind action |
| 26 | `MIN_BEHIND_ACTION_CD` | DOUBLE | NOT NULL |  | Duplicate checking minutes behind action |
| 27 | `OC_ID` | DOUBLE | NOT NULL |  | Unique identifier for order catalog item |
| 28 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | The order entry format associated to the order catalog item |
| 29 | `ORG_LONG_NAME` | VARCHAR(100) |  |  | This is the long form of the organization's name. |
| 30 | `ORG_SHORT_NAME` | VARCHAR(100) |  |  | This is the abbreviated form of the organization's name. |
| 31 | `SHORT_DESC` | VARCHAR(100) |  |  | Short description for the order catalog item |
| 32 | `SKIP_MATCH_IND` | DOUBLE |  |  | Defined as 1 skip the order catalog item. |
| 33 | `STATUS_IND` | DOUBLE |  |  | 0 - no match, 1 = exact match, 2 = one to one match, 3 =cpt4 , 5 = manual match |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

