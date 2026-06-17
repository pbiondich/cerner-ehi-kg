# LH_ABS_SECTION

> Defined groupings of Questions/Answers displayed in the Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_SECTION  
**Table type:** REFERENCE  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_ABS_SECTION_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 8 | `LH_ABS_SECTION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_ABS_SECTION table. |
| 9 | `SECTION_DISPLAY` | VARCHAR(250) |  |  | The description of the section that will be displayed in Abstractor |
| 10 | `SECTION_MEANING` | VARCHAR(50) |  |  | An identifier that uniquely identifies the section |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 14 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_ABS_LAYOUT](LH_ABS_LAYOUT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_ABS_LAYOUT](LH_ABS_LAYOUT.md) | `LH_ABS_SECTION_ID` |

