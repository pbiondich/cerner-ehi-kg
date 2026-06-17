# CP_CONCEPT_GROUP

> Define relationship Groups to apply to Concept Details

**Description:** CARE PLANNING CONCEPT GROUP  
**Table type:** REFERENCE  
**Primary key:** `CP_CONCEPT_GROUP_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_CD` | DOUBLE | NOT NULL |  | The concept code this relationship is defined for. |
| 2 | `CONCEPT_GROUP_CD` | DOUBLE | NOT NULL |  | How the entity is related to the concept |
| 3 | `CP_CONCEPT_GROUP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `INTENTION_CD` | DOUBLE | NOT NULL |  | The intention for this relationship group |
| 5 | `RULE_IND` | DOUBLE | NOT NULL |  | Equal 1 if there is a Rule associated with this relationship. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CP_CONCEPT_GROUP_DTL](CP_CONCEPT_GROUP_DTL.md) | `CP_CONCEPT_GROUP_ID` |

