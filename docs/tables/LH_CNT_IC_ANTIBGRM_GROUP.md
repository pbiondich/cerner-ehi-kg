# LH_CNT_IC_ANTIBGRM_GROUP

> Holds the group names for the antibiogram reporting solution

**Description:** LH_CNT_IC_ANTIBGRM_GROUP  
**Table type:** REFERENCE  
**Primary key:** `LH_CNT_IC_ANTIBGRM_GROUP_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_NAME` | VARCHAR(100) | NOT NULL |  | The name of the grouping |
| 2 | `GROUP_TYPE_FLAG` | DOUBLE | NOT NULL |  | Group Type Flag Values 1 = Organism Group, 2 = Encounter Group, 3 = Specimen Group |
| 3 | `LH_CNT_IC_ANTIBGRM_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CNT_IC_ANTIBGRM_GROUP table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_CNT_IC_ANTIBGRM_GROUP_R](LH_CNT_IC_ANTIBGRM_GROUP_R.md) | `LH_CNT_IC_ANTIBGRM_GROUP_ID` |
| [LH_CNT_IC_ANTIBGRM_ORG_DSC](LH_CNT_IC_ANTIBGRM_ORG_DSC.md) | `LH_CNT_IC_ANTIBGRM_GROUP_ID` |

