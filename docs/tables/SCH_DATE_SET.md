# SCH_DATE_SET

> Stores information about a scheduling date set. A date set is a group of dates associated to a scheduling template.

**Description:** Scheduling Date Set  
**Table type:** REFERENCE  
**Primary key:** `SCH_DATE_SET_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DATE_SET_TYPE_CD` | DOUBLE | NOT NULL |  | Used to identify the type of date set. Some examples are personal holiday and public holiday. |
| 3 | `DEF_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The ID of the default schedule associated to this date set. It is the primary key of the SCH_DEF_SCHED table. |
| 4 | `DESCRIPTION` | VARCHAR(200) | NOT NULL |  | The description of the date set. |
| 5 | `INCLUDE_IND` | DOUBLE | NOT NULL |  | Indicates if the resource or resource group should be included or excluded in the display. |
| 6 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | An ID to the LONG_TEXT_REFERENCE table used to associate information only text to this date set. |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A string used for identification and selection of the date set. |
| 9 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC stored in uppercase with the non-alphanumeric characters removed. |
| 10 | `SCH_DATE_SET_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is internally generated. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEF_SCHED_ID` | [SCH_DEF_SCHED](SCH_DEF_SCHED.md) | `DEF_SCHED_ID` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SCH_APPLY_LIST](SCH_APPLY_LIST.md) | `SCH_DATE_SET_ID` |
| [SCH_DATE_LINK_R](SCH_DATE_LINK_R.md) | `SCH_DATE_SET_ID` |
| [SCH_DATE_LIST](SCH_DATE_LIST.md) | `SCH_DATE_SET_ID` |

