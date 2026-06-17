# RAD_DOSE_SNOMED_RT_GLOSSARY

> The glossary for the facet and units required to display by dose facets.

**Description:** RadNet Dose SNOMED Radiation Therapy Terminology Glossary  
**Table type:** REFERENCE  
**Primary key:** `RAD_DOSE_SNOMED_RT_GLOSSARY_ID`  
**Columns:** 12  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DICOM_CODE_MEANING_TXT` | VARCHAR(256) |  |  | The meaning of the facet/unit as described in the DIACOM doc. |
| 3 | `DICOM_CODE_SCHEME_DESGNTR_TXT` | VARCHAR(256) | NOT NULL |  | An identifier of the coding organization as per the DIACOM doc. |
| 4 | `DICOM_CODE_SCHEME_VERSION_TXT` | VARCHAR(256) |  |  | Used when the coding scheme designator does not imply a version. From the DIACOM doc. |
| 5 | `DICOM_CODE_VALUE_TXT` | VARCHAR(256) | NOT NULL |  | A computer-readable and searchable identifier for a facet/unit as per the DICOM doc. |
| 6 | `DISPLAY_TXT` | VARCHAR(256) |  |  | The text that will be displayed in the front-end. |
| 7 | `RAD_DOSE_SNOMED_RT_GLOSSARY_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RAD_DOSE_SNOMED_RT_GLOSSARY table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (8)

| From table | Column |
|------------|--------|
| [OMF_RAD_DOSE_REPORT_DATA](OMF_RAD_DOSE_REPORT_DATA.md) | `BODY_PART_ID` |
| [RAD_DOSE_CONVERSION_FACTOR](RAD_DOSE_CONVERSION_FACTOR.md) | `BODY_PART_ID` |
| [RAD_DOSE_FACET_R_SET](RAD_DOSE_FACET_R_SET.md) | `UOM_ID` |
| [RAD_DOSE_FACET_R_SET_HIST](RAD_DOSE_FACET_R_SET_HIST.md) | `UOM_ID` |
| [RAD_DOSE_SCAN](RAD_DOSE_SCAN.md) | `BODY_PART_ID` |
| [RAD_DOSE_SCAN_FACET_R](RAD_DOSE_SCAN_FACET_R.md) | `UOM_ID` |
| [RAD_DOSE_SCAN_FACET_R_HIST](RAD_DOSE_SCAN_FACET_R_HIST.md) | `UOM_ID` |
| [RAD_DOSE_SCAN_HIST](RAD_DOSE_SCAN_HIST.md) | `BODY_PART_ID` |

