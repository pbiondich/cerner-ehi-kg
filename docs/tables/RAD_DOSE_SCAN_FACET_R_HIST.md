# RAD_DOSE_SCAN_FACET_R_HIST

> Stores the history of facets details for a scan.

**Description:** Radiology Dose Scan Facet Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | the person that last updated this row. |
| 4 | `RAD_DOSE_SCAN_FACET_R_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RAD_DOSE_SCAN_FACET_R_HIST table. |
| 5 | `RAD_DOSE_SCAN_FACET_R_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to the rad_dose_scan_facet_r table. Links to the row on the base table that relates to this history row. |
| 6 | `UOM_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 7 | `UOM_ID` | DOUBLE | NOT NULL | FK→ | The unit of measure for the facet. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_NBR` | DOUBLE | NOT NULL |  | The numeric value for the facet. |
| 14 | `VALUE_TXT` | VARCHAR(255) |  |  | Stores the string information related to this facet. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_DOSE_SCAN_FACET_R_ID` | [RAD_DOSE_SCAN_FACET_R](RAD_DOSE_SCAN_FACET_R.md) | `RAD_DOSE_SCAN_FACET_R_ID` |
| `UOM_ID` | [RAD_DOSE_SNOMED_RT_GLOSSARY](RAD_DOSE_SNOMED_RT_GLOSSARY.md) | `RAD_DOSE_SNOMED_RT_GLOSSARY_ID` |

