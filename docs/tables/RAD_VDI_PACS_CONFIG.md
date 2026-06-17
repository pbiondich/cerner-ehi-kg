# RAD_VDI_PACS_CONFIG

> Information related to a PACS configuration

**Description:** RadNet Virtual Desktop Integration PACS Configuration  
**Table type:** REFERENCE  
**Primary key:** `RAD_VDI_PACS_CONFIG_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_MASK` | VARCHAR(18) | NOT NULL |  | The format in which accession will be sent to the system. In our example of 0000CT201800000018, the sequence would be 1234AB123456789123. Here CT stands for Modality "Computer tomography",2018 - year in which accession was generated & 18 - accession number created for particular modality in that year. It increments by one for each accession created in particular modality. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row is considered to be valid for use. This could correspond to the active date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PACS_MODE_FLAG` | DOUBLE | NOT NULL |  | The PACS mode of operation. (0 = undefined, 1 = uni-directional, 2 = bi-directional) |
| 6 | `PACS_NAME` | VARCHAR(1000) | NOT NULL |  | The name of the PACS unit. Client entered. |
| 7 | `PACS_PARAMETERS_TXT` | VARCHAR(1000) | NOT NULL |  | Contains PACS parameteres to be passed to the PACS viewer. Command line parameteres needed to launch the third-party PACS. Example: "/cernermode or -cernermode" |
| 8 | `PACS_PATH_TXT` | VARCHAR(1000) | NOT NULL |  | The file path where the respective PACS viewer is present in the machine. |
| 9 | `PATIENT_DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of identifier being passed. |
| 10 | `RAD_VDI_PACS_CONFIG_ID` | DOUBLE | NOT NULL | PK | The unique generated number that identifies a single row on the RAD_VDI_PACS_CONFIG table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_VDI_PACS_FACILITY](RAD_VDI_PACS_FACILITY.md) | `RAD_VDI_PACS_CONFIG_ID` |

