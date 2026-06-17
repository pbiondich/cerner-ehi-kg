# UCMR_LAYOUT_FIELD_TMPLT_R

> Stores layout field relation to word processing templates for Unified Report Builder.

**Description:** Unified Case Manager Reference - Layout Field Template Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PREV_UCMR_LAYOUT_FLD_TMPLT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the layout field to template relation information. This column will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 6 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the template of this relationship. |
| 7 | `UCMR_LAYOUT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the layout field for this relationship. |
| 8 | `UCMR_LAYOUT_FIELD_TMPLT_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a layout field relationship to a word processing template for Unified Report Builder. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VIEW_SEQ` | DOUBLE | NOT NULL |  | Specifies the order in which the templates should be displayed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `UCMR_LAYOUT_FIELD_ID` | [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `UCMR_LAYOUT_FIELD_ID` |

