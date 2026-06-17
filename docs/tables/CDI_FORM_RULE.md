# CDI_FORM_RULE

> A row in this table represents a rule for when a CPDI interactive form may be required.

**Description:** CDI Form Rule  
**Table type:** REFERENCE  
**Primary key:** `CDI_FORM_RULE_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_FORM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the cdi_form table. The ID of the form the rule is associated with. |
| 2 | `CDI_FORM_RULE_ID` | DOUBLE | NOT NULL | PK | Unique row identifier for the CDI Form Rule. |
| 3 | `CRITERIA_CNT` | DOUBLE | NOT NULL |  | Specifies the number of criteria that make up this rule. |
| 4 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Specifies if forms matching this rule are required to be completed. |
| 5 | `RULE_NAME` | VARCHAR(40) | NOT NULL |  | The name of the rule. It is primarily used by the RDDS process. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_FORM_ID` | [CDI_FORM](CDI_FORM.md) | `CDI_FORM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_FORM_CRITERIA](CDI_FORM_CRITERIA.md) | `CDI_FORM_RULE_ID` |

