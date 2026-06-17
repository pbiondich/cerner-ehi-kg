# BR_LONG_TEXT

> bedrock long text

**Description:** BEDROCK LONG TEXT  
**Table type:** REFERENCE  
**Primary key:** `LONG_TEXT_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LONG_TEXT` | LONGTEXT |  |  | The long text description. |
| 2 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the table |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The id for the value on the parent_entity_name. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The table the long text is associated to. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BR_BP_ACTIVITY](BR_BP_ACTIVITY.md) | `BR_LONG_TEXT_ID` |
| [BR_BP_ACT_GROUP](BR_BP_ACT_GROUP.md) | `BR_LONG_TEXT_ID` |
| [BR_BP_ACT_LONG_DESC](BR_BP_ACT_LONG_DESC.md) | `BR_LONG_TEXT_ID` |

