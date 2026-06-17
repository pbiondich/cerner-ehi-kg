# PFT_ASSIGNMENT_RULE

> Stores the advanced assignment rule names created for the work item assignments.

**Description:** ProFit Assignment Rule  
**Table type:** REFERENCE  
**Primary key:** `PFT_ASSIGNMENT_RULE_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSIGNMENT_RULE_NAME` | VARCHAR(255) | NOT NULL |  | The name of the advanced assignment rule. |
| 3 | `ASSIGNMENT_RULE_NAME_KEY` | VARCHAR(255) | NOT NULL |  | The searchable key value of the name column. The column will contain all caps and no special characters. |
| 4 | `ENTITY_TYPE_CD` | DOUBLE | NOT NULL |  | Identies the entity type to which the rule belongs. |
| 5 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which this row is related. |
| 6 | `PFT_ASSIGNMENT_RULE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies an advanced assignment rule created for the work item assignments. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_ASSIGNMENT_CRITERIA](PFT_ASSIGNMENT_CRITERIA.md) | `PFT_ASSIGNMENT_RULE_ID` |

