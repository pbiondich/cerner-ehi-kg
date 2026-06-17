# CP_PATHWAY_ACTION

> Hold information about actions take during care planning workflow.

**Description:** Care Planning Action  
**Table type:** ACTIVITY  
**Primary key:** `CP_PATHWAY_ACTION_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | Date/Time action was taken |
| 2 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Action type taken during care planning conversation |
| 3 | `CP_COMPONENT_ID` | DOUBLE | NOT NULL | FK→ | CP Component PK value from the CP_COMPONENT table |
| 4 | `CP_NODE_ID` | DOUBLE | NOT NULL | FK→ | Care Planning node this action was taken from. |
| 5 | `CP_PATHWAY_ACTION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Provides ability to track actions by the Encounter they were taken on |
| 7 | `PATHWAY_INSTANCE_ID` | DOUBLE | NOT NULL |  | Used to group rows of activity for the same instance of a pathway. The value will be pulled from a sequence (this is not an FK field). Relates to same column in CP_PATHWAY_ACTIVITY |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID of user which took action |
| 9 | `TREATMENT_LINE_CD` | DOUBLE | NOT NULL |  | Treatment Line this action was taken for |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_COMPONENT_ID` | [CP_COMPONENT](CP_COMPONENT.md) | `CP_COMPONENT_ID` |
| `CP_NODE_ID` | [CP_NODE](CP_NODE.md) | `CP_NODE_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CP_PATHWAY_ACTION_DETAIL](CP_PATHWAY_ACTION_DETAIL.md) | `CP_PATHWAY_ACTION_ID` |

