# BMDI_ACQUIRED_RESULTS

> All results from BMDI Devices that have been mapped to an event or task assay will be captured in this table.

**Description:** BMDI Acquired Results  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACQUIRED_DT_TM` | DATETIME | NOT NULL |  | Date and time results were received from the interface and stored in CQM. |
| 2 | `CLINICAL_DT_TM` | DATETIME | NOT NULL |  | Date and Time results were captured at the device |
| 3 | `DEVICE_ID` | DOUBLE | NOT NULL |  | Devices will obtain a new instance each time they are started and transmit with results. This value comes from an external source (external to Millennium). |
| 4 | `DEVICE_PARAMETER_ID` | DOUBLE | NOT NULL | FK→ | Identifies parameter on BMDI_DEVICE_PARAMETER table |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:CLINICAL_EVENT_SEQ in CLINICAL_EVENT table. Event where this result is stored as part of verification. EVENT_ID |
| 6 | `LAB_TYPE_CD` | DOUBLE | NOT NULL |  | Laboratory Type Code |
| 7 | `MONITORED_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies device on BMDI_MONITORED_DEVICE table. |
| 8 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Nomenclature id for the parameter value |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Alternative form to identify results, currently support for sa_anesthesia_record_id. Could be expanded to others in the future. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Alternative form to identify results, currently support for sa_anesthesia_record_id |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies person who these results are for. |
| 12 | `RESULT_FORMAT_CD` | DOUBLE | NOT NULL |  | Data Format Type |
| 13 | `RESULT_ID` | DOUBLE | NOT NULL |  | Primary key for this table. |
| 14 | `RESULT_VAL` | VARCHAR(50) |  |  | Result values sent from the device. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VERIFIED_DT_TM` | DATETIME |  |  | Date and Time results were verified |
| 21 | `VERIFIED_IND` | DOUBLE | NOT NULL |  | Indicates if results were verified. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEVICE_PARAMETER_ID` | [BMDI_DEVICE_PARAMETER](BMDI_DEVICE_PARAMETER.md) | `DEVICE_PARAMETER_ID` |
| `MONITORED_DEVICE_ID` | [BMDI_MONITORED_DEVICE](BMDI_MONITORED_DEVICE.md) | `MONITORED_DEVICE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

