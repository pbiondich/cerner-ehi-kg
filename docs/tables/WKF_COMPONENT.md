# WKF_COMPONENT

> Workflow Documentation Components associated to a Workflow Session.

**Description:** Workflow Component  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_CONCEPT` | VARCHAR(256) | NOT NULL |  | Identifies which type of documentation component this component this is |
| 2 | `COMPONENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID for the data row in the Component Entity Name table for this Component. |
| 3 | `COMPONENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The Name of the Table that contains the data for this Workflow Component |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `WKF_COMPONENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the WKF_COMPONENT table. |
| 10 | `WKF_WORKFLOW_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Parent Workflow Session |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WKF_WORKFLOW_ID` | [WKF_WORKFLOW](WKF_WORKFLOW.md) | `WKF_WORKFLOW_ID` |

