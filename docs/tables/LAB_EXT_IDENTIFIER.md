# LAB_EXT_IDENTIFIER

> Table to store external identifiers used within interoperability.

**Description:** Lab External Identifier  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AP_EXT_DATA_ID` | DOUBLE |  |  | Unique identifier from the ap external data table to which this identifier is associated. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter associated to the parent of this identifier. Included to facilitate crawling needs. |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | The identiifer for the clinical event to which this identifier is associated |
| 5 | `GEN_LAB_EXT_DATA_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the general lab external data table to which this identifier is associated. |
| 6 | `LAB_EXT_IDENTIFIER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LAB_EXT_IDENTIFIER table. |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `MICRO_SEQ_NBR` | DOUBLE |  |  | Specifc for Microbiology, Used for uniqueness in cases where there are multiple micro records |
| 9 | `MIC_EXT_DATA_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the MIC_EXT_DATA table. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person associated to the parent of this identifier. Included to facilitate crawling needs. |
| 11 | `SYSTEM_URI` | VARCHAR(80) | NOT NULL |  | The URI of the system that assigned the value. If value is not null then the combo of system and value is unique. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `VALUE_TXT` | VARCHAR(200) |  |  | The value of the identifier. May be null if Rendered Value is not null. If valued, is unique when combined with system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `GEN_LAB_EXT_DATA_ID` | [GEN_LAB_EXT_DATA](GEN_LAB_EXT_DATA.md) | `GEN_LAB_EXT_DATA_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `MIC_EXT_DATA_ID` | [MIC_EXT_DATA](MIC_EXT_DATA.md) | `MIC_EXT_DATA_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

