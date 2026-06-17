# EEM_FILE

> ABN Data Files

**Description:** ABN Data File  
**Table type:** REFERENCE  
**Primary key:** `EEM_FILE_ID`  
**Columns:** 22  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHECK_SEQ` | DOUBLE | NOT NULL |  | This field denotes the current content version used for ABN code pair checking. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 9 | `EEM_FILE_ID` | DOUBLE | NOT NULL | PK | This is a unique identifier for the ABN data file |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `IMPORT_SEQ` | DOUBLE | NOT NULL |  | This field denotes the last content version that was imported for the file. |
| 12 | `INFO_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 13 | `INPATIENT_IND` | DOUBLE | NOT NULL |  | Denotes if the context of the Data File apply to Inpatient |
| 14 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 15 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 16 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 17 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SYSTEM_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `INFO_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `EEM_FILE_ID` |
| [EEM_ABN_DATA](EEM_ABN_DATA.md) | `EEM_FILE_ID` |
| [EEM_ABN_RULE](EEM_ABN_RULE.md) | `EEM_FILE_ID` |
| [EEM_FILE_ACTION](EEM_FILE_ACTION.md) | `EEM_FILE_ID` |
| [EEM_FILE_CHECK](EEM_FILE_CHECK.md) | `EEM_FILE_ID` |
| [EEM_FILE_RELTN](EEM_FILE_RELTN.md) | `EEM_FILE_ID` |
| [EEM_IMPORT_DATA](EEM_IMPORT_DATA.md) | `EEM_FILE_ID` |

