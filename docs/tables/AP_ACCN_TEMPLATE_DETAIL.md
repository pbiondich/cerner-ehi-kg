# AP_ACCN_TEMPLATE_DETAIL

> This reference table includes Accessioning Template parameters that have been established and saved. Accessioning templates allow a site to predefine default values for the various fields within the accessioning conversation.

**Description:** AP Accessioning Template Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CARRY_FORWARD_IND` | DOUBLE |  |  | This field identifies whether the value from this row should be carried forward from one case to the next during the accessioning process. |
| 2 | `CARRY_FORWARD_SPEC_IND` | DOUBLE |  |  | This field identifies whether the value from this row should be carried forward from one specimen to the next during the accessioning process. This indicator is only used when adding additional specimens to a pathology case. |
| 3 | `DETAIL_FLAG` | DOUBLE |  |  | This field contains a representation of the type of data included in this template detail -- no value, data determined by the detail_id, or data determined by the detail_name. |
| 4 | `DETAIL_ID` | DOUBLE |  |  | This field contains the internal identification code of the 'template detail' value within a specified template parameter (denoted in the DETAIL_NAME field). Note this field is only used when the DETAIL_FLAG contains a value of 1. |
| 5 | `DETAIL_NAME` | VARCHAR(16) |  |  | This field represents the type of template detail (order location, requesting physician, specimen code, collected date/time) associated with this row on the 'ap accession template detail' table. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Name of the Parent table for the Template Detail. The internal identifier is stored in the DETAIL_ID column. |
| 7 | `TEMPLATE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal reference to codeset 16689 which contains the user-defined 'Accessioning Template' name. At the time 'template' parameters are saved, the user is required to enter a name for the template, and this name is saved to codeset 16689. |
| 8 | `TEMPLATE_DETAIL_ID` | DOUBLE | NOT NULL |  | This field contains the unique value representing the 'accessioning template' detail. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TEMPLATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

