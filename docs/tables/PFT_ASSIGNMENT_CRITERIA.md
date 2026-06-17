# PFT_ASSIGNMENT_CRITERIA

> Stores the criterias built for each of the advanced assignment rules.

**Description:** ProFit Assignment Criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CRITERIA_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the row related to the entity |
| 3 | `CRITERIA_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies the parent entity to which this criteria is related. |
| 4 | `CRITERIA_NAME` | VARCHAR(50) | NOT NULL |  | Defines the criteria token which is represented by this row. |
| 5 | `GROUP_NBR` | DOUBLE | NOT NULL |  | This will represtne to which row the criteria belongs, so the individual rows can be grouped within a rule. |
| 6 | `PFT_ASSIGNMENT_CRITERIA_ID` | DOUBLE | NOT NULL |  | Uniquely identifies criteria built for each of the advanced assignment rules. |
| 7 | `PFT_ASSIGNMENT_RULE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related assignment rule. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_TXT` | VARCHAR(50) | NOT NULL |  | Contains the text value for the criteria. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_ASSIGNMENT_RULE_ID` | [PFT_ASSIGNMENT_RULE](PFT_ASSIGNMENT_RULE.md) | `PFT_ASSIGNMENT_RULE_ID` |

