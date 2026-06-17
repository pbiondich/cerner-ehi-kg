# INVEST_AGENT_DEV

> This table contains information about investigational agents or devices being used in the protocol.

**Description:** Contains info about investigational agents or devices being used in the protocol  
**Table type:** REFERENCE  
**Primary key:** `INVEST_AGENT_DEV_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGENT_DEV_ID` | DOUBLE | NOT NULL |  | A logical identifier into the invest_agent_dev table. No two active rows (with end_effective_dt_tm of 31-dec-2100) will have the same agent_dev_id |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `INVEST_AGENT_DEV_CD` | DOUBLE | NOT NULL |  | This field contains a code indicating an investigational agent or device being used in the protocol/study. |
| 5 | `INVEST_AGENT_DEV_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the invest_agent_dev table. It is an internal system assigned number. |
| 6 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_amendment table. This field identifies the protocol amendment that is using the investigational agent or device |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [INVEST_DEV](INVEST_DEV.md) | `AGENT_DEV_ID` |
| [INVEST_NEW_DRUG](INVEST_NEW_DRUG.md) | `AGENT_DEV_ID` |

