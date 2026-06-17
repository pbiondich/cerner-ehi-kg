# BR_ADO_DETAIL

> Stores the relations for Topic, Scenario, Facility and Category.

**Description:** Bedrock Advisor Orders Detail  
**Table type:** REFERENCE  
**Primary key:** `BR_ADO_DETAIL_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ADO_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Category, Foreign Key from BR_ADO_CATEGORY |
| 2 | `BR_ADO_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_ADO_DETAIL table. |
| 3 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Facility to which Advisor Orders are being defined. |
| 4 | `NOTE_TXT` | VARCHAR(255) |  |  | Any required Notes at the Category Level. |
| 5 | `SCENARIO_CATEGORY_SEQ` | DOUBLE | NOT NULL |  | Sequence that categories per scenario are to be display in the Advisor frontend. |
| 6 | `SCENARIO_MEAN` | VARCHAR(50) | NOT NULL |  | Identifies the Scenario that this detail pertains to. |
| 7 | `SELECT_IND` | DOUBLE | NOT NULL |  | Determines if single or multiples choices can be made per category. 1-Single Select, 2-Multi Select |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_ADO_CATEGORY_ID` | [BR_ADO_CATEGORY](BR_ADO_CATEGORY.md) | `BR_ADO_CATEGORY_ID` |
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BR_ADO_OPTION](BR_ADO_OPTION.md) | `BR_ADO_DETAIL_ID` |
| [BR_ADO_ORD_LIST](BR_ADO_ORD_LIST.md) | `BR_ADO_DETAIL_ID` |

