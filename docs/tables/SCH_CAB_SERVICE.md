# SCH_CAB_SERVICE

> This table is used for defining Choose and Book services

**Description:** Scheduling Choose and Book services  
**Table type:** REFERENCE  
**Primary key:** `CAB_SERVICE_ID`  
**Columns:** 23  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_SYNONYM_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling appointment type. |
| 6 | `CAB_SERVICE_ALIAS` | VARCHAR(100) | NOT NULL |  | NHS's unique identifier for this service |
| 7 | `CAB_SERVICE_ID` | DOUBLE | NOT NULL | PK | The unique identifier of the scheduling Choose and Book Service. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `DESCRIPTION` | VARCHAR(255) |  |  | A long description used for documentation. |
| 10 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The encounter type code |
| 11 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location the service will be booked into. |
| 13 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The treatment function code |
| 14 | `MNEMONIC` | VARCHAR(100) |  |  | A 100-character string used for identification and selection. |
| 15 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 16 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 17 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 18 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The DOH specialty code |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_SYNONYM_CD` | [SCH_APPT_SYN](SCH_APPT_SYN.md) | `APPT_SYNONYM_CD` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SCH_CAB_RES](SCH_CAB_RES.md) | `CAB_SERVICE_ID` |
| [SCH_CAB_SLOT](SCH_CAB_SLOT.md) | `CAB_SERVICE_ID` |
| [SCH_SLOT_ALIAS](SCH_SLOT_ALIAS.md) | `CAB_SERVICE_ID` |

