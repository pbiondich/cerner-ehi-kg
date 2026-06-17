# RAD_DOSE_SCAN

> Represents a single radiation scan.

**Description:** RadNet Dose Scan  
**Table type:** ACTIVITY  
**Primary key:** `RAD_DOSE_SCAN_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | This field contains a code that identifies the dose template modality used for this scan. |
| 2 | `BODY_PART_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 3 | `BODY_PART_ID` | DOUBLE | NOT NULL | FK→ | The body part the conversion factor applies to. |
| 4 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | Date/time the row was created. |
| 5 | `EFFECTIVE_DOSE_AMT` | DOUBLE | NOT NULL |  | The calculated effective dose for the scan. |
| 6 | `IRRADIATION_EVENT_UID` | VARCHAR(255) | NOT NULL |  | Stores the irradiation event uid received from DICOM. |
| 7 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | Date/time the row was last updated. |
| 8 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that last updated this row. |
| 9 | `RAD_DOSE_SCAN_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RAD_DOSE_SCAN table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BODY_PART_ID` | [RAD_DOSE_SNOMED_RT_GLOSSARY](RAD_DOSE_SNOMED_RT_GLOSSARY.md) | `RAD_DOSE_SNOMED_RT_GLOSSARY_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [OMF_RAD_DOSE_REPORT_DATA](OMF_RAD_DOSE_REPORT_DATA.md) | `RAD_DOSE_SCAN_ID` |
| [RAD_DOSE_SCAN_FACET_R](RAD_DOSE_SCAN_FACET_R.md) | `RAD_DOSE_SCAN_ID` |
| [RAD_DOSE_SCAN_HIST](RAD_DOSE_SCAN_HIST.md) | `RAD_DOSE_SCAN_ID` |
| [RAD_DOSE_SCAN_ORDER_R](RAD_DOSE_SCAN_ORDER_R.md) | `RAD_DOSE_SCAN_ID` |

