# INSTRUMENT_PROTOCOL

> Stores the protocols for an instrument type.

**Description:** Instrument Protocol  
**Table type:** REFERENCE  
**Primary key:** `INSTRUMENT_PROTOCOL_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `INSTRUMENT_PROTOCOL_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the protocol for an instrument type. |
| 3 | `INSTRUMENT_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the code value for the staining instrument type. |
| 4 | `PLACER_FIELD_1` | VARCHAR(60) | NOT NULL |  | This field provides additional information to the instrument such as the label template (OBR - 18 in HL7 message). |
| 5 | `PROC_CODE_TXT` | VARCHAR(250) | NOT NULL |  | Specific procedure code for the universal service identifier (OBR - 44 in HL7 message). |
| 6 | `PROTOCOL_NAME` | VARCHAR(50) | NOT NULL |  | Contains the free text description of the instrument protocol. |
| 7 | `SUPLMTL_SERV_INFO_TXT` | VARCHAR(250) | NOT NULL |  | Describes additional service information for the universal service identifier (OBR - 46 in HL7 message). |
| 8 | `UNIVERSAL_SERVICE_IDENT` | VARCHAR(250) | NOT NULL |  | The string identifier of the instrument protocol (OBR - 4 in HL7 message). |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PROC_INSTRMT_PROTCL_R](PROC_INSTRMT_PROTCL_R.md) | `INSTRUMENT_PROTOCOL_ID` |
| [TASK_INSTRMT_PROTCL_R](TASK_INSTRMT_PROTCL_R.md) | `INSTRUMENT_PROTOCOL_ID` |

