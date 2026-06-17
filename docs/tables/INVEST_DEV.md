# INVEST_DEV

> Contains information about investigational device

**Description:** INVEST DEV  
**Table type:** REFERENCE  
**Primary key:** `INVEST_DEV_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGENT_DEV_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the agent |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DEVICE_ID` | DOUBLE | NOT NULL | FK→ | A unique key for the Investigation Device on a protocol. No two active rows can have the same Device_id. |
| 4 | `DEVICE_NAME` | VARCHAR(20) |  |  | Free text name of the investigational device |
| 5 | `DEVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Classification of the device / Classification of investigational drug. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `INVEST_DEVICE_NBR_TXT` | VARCHAR(12) | NOT NULL |  | Textual investigational device number. |
| 8 | `INVEST_DEV_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AGENT_DEV_ID` | [INVEST_AGENT_DEV](INVEST_AGENT_DEV.md) | `INVEST_AGENT_DEV_ID` |
| `DEVICE_ID` | [INVEST_DEV](INVEST_DEV.md) | `INVEST_DEV_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INVEST_DEV](INVEST_DEV.md) | `DEVICE_ID` |

