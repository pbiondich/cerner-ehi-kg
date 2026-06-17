# RAD_DOSE_FACET_MODALITY

> Stores the relationship between dose facets and modality.

**Description:** RadNet Dose Facet Modality Relation  
**Table type:** REFERENCE  
**Primary key:** `RAD_DOSE_FACET_MODALITY_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | This field contains a code that identifies the dose template modality used for this scan. |
| 3 | `CONTROL_NAME` | VARCHAR(255) | NOT NULL |  | The name of the specific database setting. |
| 4 | `DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | Bitmap indicating the data expected for this facet_cd for the modality. |
| 5 | `FACET_CD` | DOUBLE | NOT NULL |  | The radiation dose facet tied to the modality (activity_subtype_cd) |
| 6 | `FACET_SEQ` | DOUBLE | NOT NULL |  | The order the facet should appear in the application for the given activity subtype. |
| 7 | `RAD_DOSE_FACET_MODALITY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RAD_DOSE_FACET_MODALITY table. |
| 8 | `RESP_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates if this facet should be displayed in the front end application. 0 - Unchecked (no need to show this facet), 1 - Checked (need to show this facet), 3 - Checked and Disabled (need to show this facet. User cannot modify this setting.) |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_DOSE_SCAN_FACET_R](RAD_DOSE_SCAN_FACET_R.md) | `RAD_DOSE_FACET_MODALITY_ID` |

