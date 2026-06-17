# SCH_DISP_SCHEME

> Contains the display attributes for scheduling objects.

**Description:** Display Scheme  
**Table type:** REFERENCE  
**Primary key:** `DISP_SCHEME_ID`  
**Columns:** 35  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BACK_COLOR` | DOUBLE |  |  | The numeric equilivant of the background color. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BORDER_COLOR` | DOUBLE |  |  | The numeric equilivant of the border color. |
| 8 | `BORDER_SIZE` | DOUBLE |  |  | The numeric equilivant of the border size. |
| 9 | `BORDER_STYLE` | DOUBLE |  |  | The numeric equilivant of the border style. |
| 10 | `BRUSH_TYPE` | DOUBLE |  |  | The numeric equilivant of the brush type. |
| 11 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 12 | `DAYS_OF_WEEK` | VARCHAR(7) |  |  | A 7-char string representing the days of the week. |
| 13 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 14 | `DISP_SCHEME_ID` | DOUBLE | NOT NULL | PK | The coded identifier of the disp scheme. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `FORE_COLOR` | DOUBLE |  |  | The numeric equilivant of the foreground color. |
| 17 | `HATCH_COLOR` | DOUBLE |  |  | The numeric equilivant of the hatching color. |
| 18 | `HATCH_STYLE` | DOUBLE |  |  | The numeric equilivant of the hatching style. |
| 19 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 20 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 21 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 22 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 23 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 24 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 25 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 26 | `PEN_SHAPE` | DOUBLE |  |  | A "0" in this column will indicate a "square" border pen. A "1" in this column will represent a "round" border pen. |
| 27 | `RELEASE_INTERVAL` | DOUBLE |  |  | The time interval in minutes before the display should expire. |
| 28 | `SCHEME_TYPE_FLAG` | DOUBLE | NOT NULL |  | Deteremines the usage of the display scheme. |
| 29 | `SHAPE` | DOUBLE |  |  | The numeric equilivant of the shape. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 35 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [SCH_ACTIVITY](SCH_ACTIVITY.md) | `DISP_SCHEME_ID` |
| [SCH_APPT](SCH_APPT.md) | `APPT_SCHEME_ID` |
| [SCH_APPT](SCH_APPT.md) | `SLOT_SCHEME_ID` |
| [SCH_APPT_BOOK](SCH_APPT_BOOK.md) | `DISP_SCHEME_ID` |
| [SCH_APPT_DEF](SCH_APPT_DEF.md) | `SLOT_SCHEME_ID` |
| [SCH_APPT_STATE](SCH_APPT_STATE.md) | `DISP_SCHEME_ID` |
| [SCH_BASE_SCHEDULE_ACTIVITY](SCH_BASE_SCHEDULE_ACTIVITY.md) | `ACTIVITY_SCHEME_ID` |
| [SCH_DEF_SLOT](SCH_DEF_SLOT.md) | `SLOT_SCHEME_ID` |
| [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `DISP_SCHEME_ID` |

