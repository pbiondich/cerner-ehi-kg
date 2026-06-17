# CNT_DS_LABEL_KEY

> Used to build data to be imported into DYNAMIC_LABEL_TEMPLATE.

**Description:** Content Doc Set Label Key  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CNT_DS_LABEL_KEY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CNT_DS_LABEL_KEY table. |
| 3 | `CNT_DS_LABEL_KEY_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of label in conjunction with version_dt_tm column |
| 4 | `ENCOUNTER_SPECIFIC_IND` | DOUBLE | NOT NULL |  | This field indicates if a label created from this template is intended to be active only during a single encounter or if it spans multiple encounters |
| 5 | `LABEL_TEMPLATE_ID` | DOUBLE | NOT NULL |  | ID of the dynamic label template which is part of the doc set |
| 6 | `LABEL_TEMPLATE_REF_ID` | DOUBLE |  | FK→ | When the configuration is imported from from .xml/.czf to this table, ithis column will be populated with a null value.When Bedrock tool maps this record, it will be updated to the parent row from DYNAMIC_LABEL_TEMPLATE. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | Date and time when this record was updated, used in versioning of the label in conjunction with UID column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LABEL_TEMPLATE_REF_ID` | [DYNAMIC_LABEL_TEMPLATE](DYNAMIC_LABEL_TEMPLATE.md) | `LABEL_TEMPLATE_ID` |

