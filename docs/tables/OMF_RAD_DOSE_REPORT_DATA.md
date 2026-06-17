# OMF_RAD_DOSE_REPORT_DATA

> The OMFtable referred by a Dose discern report, that contains information about dose data added for any selected order.

**Description:** OMF RadNet Dose Report Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACQUISITION_TYPE_TXT` | VARCHAR(255) |  |  | Value of the Acquisition Type dose parameter. |
| 2 | `ANODE_TARGET_MATERIAL_TXT` | VARCHAR(255) |  |  | Contains value of Anode Target Material dose parameter. |
| 3 | `AVERAGE_GLANDULAR_DOSE_NBR` | DOUBLE |  |  | Contains value of Average glandular dose parameter |
| 4 | `BODY_PART_ID` | DOUBLE | NOT NULL | FK→ | The body part this report detail data pertains to. |
| 5 | `COMPRESSION_THICKNESS_NBR` | DOUBLE |  |  | Contains value of Compression Thickness dose parameter |
| 6 | `CTDIW_PHANTOM_TYPE_TXT` | VARCHAR(255) |  |  | Contains value of CTDIw Phantom Type dose parameter |
| 7 | `CTDI_NBR` | DOUBLE |  |  | Contains value of CTDI dose parameter |
| 8 | `DAP_NBR` | DOUBLE |  |  | Contains value of DAP dose parameter |
| 9 | `DLP_NBR` | DOUBLE |  |  | Contains value of DLP dose parameter |
| 10 | `DOSE_RP_NBR` | DOUBLE |  |  | Contains value of Dose RP dose parameter |
| 11 | `EFFECTIVE_DOSE_NBR` | DOUBLE |  |  | Contains value of Effective dose parameter |
| 12 | `ENTRANCE_EXPOSURE_RP_NBR` | DOUBLE |  |  | Contains value of Entrance Exposure RP dose parameter |
| 13 | `KVP_NBR` | DOUBLE |  |  | Contains value of KvP dose parameter |
| 14 | `MAS_NBR` | DOUBLE |  |  | Contains value of mAs dose parameter |
| 15 | `MODALITY_CD` | DOUBLE | NOT NULL |  | This field contains a code that identifies the dose template modality used for this scan. |
| 16 | `OMF_RAD_DOSE_REPORT_DATA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the omf_Rad_dose_report_data table. |
| 17 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Contains the order_ID of the order, for which dose data is being added. |
| 18 | `PARAMETER_VALUE_SEQ` | DOUBLE |  |  | Used to identify the number of dose scans that were added for the selected order. Each dose scan will have a unique whole number. Most rows will have a decimal .01. If multiple rows are required to store all the information for a scan, the decimal part is incremented. |
| 19 | `PITCH_FACTOR_NBR` | DOUBLE |  |  | Contains value of Pitch Factor dose parameter |
| 20 | `RADIONUCLIDE_ACTIVITY_NBR` | DOUBLE |  |  | Contains value of Radionuclide Activity dose parameter |
| 21 | `RADIONUCLIDE_NBR` | DOUBLE |  |  | *** Obsolete *** |
| 22 | `RADIONUCLIDE_TXT` | VARCHAR(255) |  |  | Contains value of Radionuclide dose parameter |
| 23 | `RADIOPHARMACEUTICAL_NBR` | DOUBLE |  |  | *** Obsolete *** |
| 24 | `RADIOPHARMACEUTICAL_TXT` | VARCHAR(255) |  |  | Contains value of Radio pharmaceutical dose parameter |
| 25 | `RAD_DOSE_SCAN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the scan that this report row pertains to. |
| 26 | `REFERENCE_POINT_DEFINITION_TXT` | VARCHAR(255) |  |  | Contains value of Reference Point Definition dose parameter |
| 27 | `SCANNING_LENGTH_NBR` | DOUBLE |  |  | Contains value of Scanning length dose parameter |
| 28 | `SSDE_MEASUREMENT_TEXT` | VARCHAR(255) |  |  | contains value of SSDE measurement dose parameter |
| 29 | `SSDE_NBR` | DOUBLE |  |  | contains value of SSDE dose parameter |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 35 | `XRAY_FILTER_MATERIAL_TXT` | VARCHAR(255) |  |  | Contains value of X-Ray Filter Material dose parameter |
| 36 | `XRAY_FILTER_THICKNESS_MAX_NBR` | DOUBLE |  |  | Contains value of X-Ray Filter Thickness Maximum dose parameter |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BODY_PART_ID` | [RAD_DOSE_SNOMED_RT_GLOSSARY](RAD_DOSE_SNOMED_RT_GLOSSARY.md) | `RAD_DOSE_SNOMED_RT_GLOSSARY_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RAD_DOSE_SCAN_ID` | [RAD_DOSE_SCAN](RAD_DOSE_SCAN.md) | `RAD_DOSE_SCAN_ID` |

