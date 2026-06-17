# SN_RPT_FILTER

> This table holds all of the filters for a given filter group.

**Description:** SN RPT FILTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTROL_EVENT_CD` | DOUBLE | NOT NULL |  | The event code associated with the task_assay_cd |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was initially inserted. |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 5 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that created the row. |
| 6 | `FILTER_STRING` | VARCHAR(255) |  |  | This holds non-foreign key filter values. |
| 7 | `FORM_EVENT_CD` | DOUBLE | NOT NULL |  | The event code associated with the input_form_cd |
| 8 | `INPUT_FORM_CD` | DOUBLE | NOT NULL |  | For a clinical event filter, this will contain the code value of the form to which the filter value applies. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | If this filter has a value that is a foreign key to another table, this will be the foreign key value with the table in the parent_entity_name column. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the table that this filter has a foreign key to. |
| 11 | `RPT_FILTER_GRP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key into the SN_RPT_FILTER_GRP table to indicate which filter group this filter belongs to. |
| 12 | `RPT_FILTER_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 13 | `RPT_FILTER_REF_ID` | DOUBLE | NOT NULL |  | Foreign key into the SN_RPT_FILTER_REF table to indicate what reference filter this filter was created from. |
| 14 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | For a clinical event filter, this will contain the code value of the control to which the filter value applies. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RPT_FILTER_GRP_ID` | [SN_RPT_FILTER_GRP](SN_RPT_FILTER_GRP.md) | `RPT_FILTER_GRP_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

