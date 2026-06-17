# EEM_NETWORK

> Attributes for a provider Network

**Description:** Provider Networks  
**Table type:** REFERENCE  
**Primary key:** `NETWORK_ID`  
**Columns:** 18  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DESCRIPTION` | VARCHAR(200) |  |  | Description of Network |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Long Text Id of the Comment for a Network |
| 9 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | Network mnemonic |
| 10 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | Mnemonic Key field |
| 11 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 12 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | International version of mnemonic key |
| 13 | `NETWORK_ID` | DOUBLE | NOT NULL | PK | Primary Key. |
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

## Referenced by (3)

| From table | Column |
|------------|--------|
| [EEM_ENTITY_NTWK_RELTN](EEM_ENTITY_NTWK_RELTN.md) | `NETWORK_ID` |
| [EEM_NTWK_PRSNL_RELTN](EEM_NTWK_PRSNL_RELTN.md) | `NETWORK_ID` |
| [EEM_PRSNL_LOC_RELTN](EEM_PRSNL_LOC_RELTN.md) | `NETWORK_ID` |

