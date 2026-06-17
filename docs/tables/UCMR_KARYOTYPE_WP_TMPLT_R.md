# UCMR_KARYOTYPE_WP_TMPLT_R

> This table maintains an association between a standard karyotype and 1 or more word processing templates for a given facility. If the facility code is not specified it will be assumed that this word processing template can be used throughout all facilities.

**Description:** Unified Case Manager Reference - Karyotype Word Processing Template Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PREV_UCMR_KARYOTYP_WP_TMPLT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the karyotype and word processing template relationships. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 6 | `UCMR_KARYOTYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Karyotype involved in this relationship. |
| 7 | `UCMR_KARYOTYP_WP_TMPLT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between a karyotype and a word processing template. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `WP_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the word processing template involved in this relationship. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_KARYOTYPE_ID` | [UCMR_KARYOTYPE](UCMR_KARYOTYPE.md) | `UCMR_KARYOTYPE_ID` |
| `WP_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

