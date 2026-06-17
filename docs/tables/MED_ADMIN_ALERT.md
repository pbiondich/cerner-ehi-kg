# MED_ADMIN_ALERT

> Medication Administration Alert Table

**Description:** Medication Administration Alert  
**Table type:** ACTIVITY  
**Primary key:** `MED_ADMIN_ALERT_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_SEVERITY_CD` | DOUBLE | NOT NULL |  | The severity of the recorded alert. |
| 2 | `ALERT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of alert recorded. |
| 3 | `CAREAWARE_USED_IND` | DOUBLE | NOT NULL |  | Maintains whether CareAware was used to obtain drug related information. |
| 4 | `EVENT_DT_TM` | DATETIME | NOT NULL |  | The date/time that the alert was presented to the user. |
| 5 | `MED_ADMIN_ALERT_ID` | DOUBLE | NOT NULL | PK | The ID of the medication administration alert event. |
| 6 | `MED_ADMIN_EVENT_ID` | DOUBLE | NOT NULL | FK→ | A unique ID that identifies a specific medication event on the med_admin_event Table |
| 7 | `NEXT_CALC_DT_TM` | DATETIME |  |  | Date and time of the next calculated administration. |
| 8 | `NEXT_CALC_TZ` | DOUBLE | NOT NULL |  | Time zone for the next calculated administration. |
| 9 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The nurse unit of the device the user is using to enter the medication admin event. |
| 10 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position of the user documenting the medication admin event. |
| 11 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the user documenting the medication admin event. |
| 12 | `SOURCE_APPLICATION_FLAG` | DOUBLE |  |  | Identification for source application used to chart med event. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MED_ADMIN_EVENT_ID` | [MED_ADMIN_EVENT](MED_ADMIN_EVENT.md) | `MED_ADMIN_EVENT_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MED_ADMIN_MED_ERROR](MED_ADMIN_MED_ERROR.md) | `MED_ADMIN_ALERT_ID` |
| [MED_ADMIN_PT_ERROR](MED_ADMIN_PT_ERROR.md) | `MED_ADMIN_ALERT_ID` |

