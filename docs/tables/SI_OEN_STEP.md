# SI_OEN_STEP

> Definition of steps used in the open engine processes

**Description:** Open Engine Step  
**Table type:** REFERENCE  
**Primary key:** `SI_OEN_STEP_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of the step |
| 2 | `SI_OEN_STEP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `STEP_NAME` | VARCHAR(100) | NOT NULL |  | Name of the step |
| 4 | `STEP_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | ID that links to the configuration properties for the step |
| 5 | `STEP_TYPE` | VARCHAR(100) | NOT NULL |  | The class name of the step |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STEP_PROPERTY_ID` | [SI_OEN_PROPERTY](SI_OEN_PROPERTY.md) | `SI_OEN_PROPERTY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_OEN_SUBSCRIPTION_STEP_R](SI_OEN_SUBSCRIPTION_STEP_R.md) | `SI_OEN_STEP_ID` |

