# CT_RN_PROT_CONFIG

> Store the research network run data.

**Description:** Research Network Protocol Configuration  
**Table type:** REFERENCE  
**Primary key:** `CT_RN_PROT_CONFIG_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CONFIG_INFO` | VARCHAR(4000) |  |  | The configuration data string defining parameters used by the research network. |
| 3 | `CONFIG_VERSION_NBR` | DOUBLE | NOT NULL |  | The version of the configuration that was last saved. |
| 4 | `CT_RN_PROT_CONFIG_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 5 | `DATA_EXTRACT_CAP_FLAG` | DOUBLE | NOT NULL |  | Indicates if the research network protocol can have data extraction enabled. Available options are: 0 - Not capable of doing data extraction 1 - Capable of doing data extraction but it is disabled. 2 - Capable of doing data extraction and it is enabled. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | this field uniquely identifies a row in the long_text_reference table. |
| 8 | `PREV_CT_RN_PROT_CONFIG_ID` | DOUBLE | NOT NULL | FK→ | the original value of ct_rn_prot_config_id used for grouping the related versions. required for type 2 versioning methodology. |
| 9 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | this field uniquely identifies a row in the prot_master table. |
| 10 | `PROT_PASSWORD` | VARCHAR(100) | NOT NULL |  | Encrypted password used to authorize changing research network protocols mode. |
| 11 | `RN_PROTOCOL_CD` | DOUBLE | NOT NULL |  | This field contains the code for the protocol that is used to determine active status of the research network protocol |
| 12 | `SOURCE_FILENAME` | VARCHAR(255) |  |  | This field identifies the filename that was used during package installation for the research protocol. |
| 13 | `STOP_DT_TM` | DATETIME |  |  | The date/time after which the protocol will no longer be run through the research network |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `PREV_CT_RN_PROT_CONFIG_ID` | [CT_RN_PROT_CONFIG](CT_RN_PROT_CONFIG.md) | `CT_RN_PROT_CONFIG_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CT_RN_PROT_CONFIG](CT_RN_PROT_CONFIG.md) | `PREV_CT_RN_PROT_CONFIG_ID` |

