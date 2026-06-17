# CDI_RULE

> Defines a rule used to determine if the associated parent entity matches another entity's metadata.

**Description:** CDI Rule  
**Table type:** REFERENCE  
**Primary key:** `CDI_RULE_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_RULE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CDI_RULE table. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains the identifier for the parent table row. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This field contains the name of table that this cdi_rule row is associated to. |
| 4 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates if the parent entity matching this rule should be considered required. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_RULE_CRITERIA](CDI_RULE_CRITERIA.md) | `CDI_RULE_ID` |

