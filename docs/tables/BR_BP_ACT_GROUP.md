# BR_BP_ACT_GROUP

> Stores default activity groups built by bedrock

**Description:** Bedrock BP Act Group  
**Table type:** REFERENCE  
**Primary key:** `BR_BP_ACT_GROUP_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACT_GROUP_MEAN` | VARCHAR(100) |  |  | Unique meaning for the activity group |
| 2 | `BLUEPRINT_IND` | DOUBLE |  |  | Indicates blueprint or not |
| 3 | `BR_BP_ACT_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique ID |
| 4 | `BR_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ID of long description for the activity group |
| 5 | `CAT_DISP` | VARCHAR(100) |  |  | Solution display |
| 6 | `CAT_MEAN` | VARCHAR(200) |  |  | Solution meaning |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | Date and time the blueprint was created |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | ID of the person who created the blueprint |
| 9 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of the activity group |
| 10 | `DISPLAY` | VARCHAR(100) |  |  | Display for the activity group |
| 11 | `DISPLAY_KEY_CAP` | VARCHAR(100) |  |  | Display for the activity group, stored as all caps |
| 12 | `TYPE_FLAG` | DOUBLE |  |  | Indicates how a blueprints tasks are to be completed |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERSION_NBR` | DOUBLE |  |  | Indicates the version of the activity group |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_LONG_TEXT_ID` | [BR_LONG_TEXT](BR_LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_BP_ACT_GROUP_R](BR_BP_ACT_GROUP_R.md) | `BR_BP_ACT_GROUP_ID` |

