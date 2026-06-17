# UCM_DSR_VARIANT_INFO

> Stores property values for a variant.

**Description:** Unified Case Manager - Document Sequencing Results Variant Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `COLUMN_CD` | DOUBLE | NOT NULL |  | The column associated with the orderable for this specific variant info property instance |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `INFO_CD` | DOUBLE | NOT NULL |  | The code set for this field may vary depending on the column_cd. For example, the Gene column will have a different code set for infor_cd than the Variant Classification Column. |
| 7 | `INFO_NBR` | DOUBLE | NOT NULL |  | Contains the result for numeric variant properties. |
| 8 | `INFO_TXT` | VARCHAR(250) |  |  | Contains the human readable result for this variant property. |
| 9 | `PREV_UCM_DSR_VARIANT_INFO_ID` | DOUBLE | NOT NULL |  | Used to track versions of the dsr variant information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 10 | `UCM_DSR_VARIANT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related DSR Variant. |
| 11 | `UCM_DSR_VARIANT_INFO_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a property value for a variant. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCM_DSR_VARIANT_ID` | [UCM_DSR_VARIANT](UCM_DSR_VARIANT.md) | `UCM_DSR_VARIANT_ID` |

