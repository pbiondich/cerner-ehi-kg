# MM_DB_LOG

> ProCure DB update logging table.

**Description:** MM DB LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 60

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APP_NAME` | VARCHAR(60) |  |  | The application which caused the insert. |
| 2 | `ATTR_COUNT` | DOUBLE |  |  | The number of attributes filled out for a specific row. |
| 3 | `ATTR_ID1` | DOUBLE |  |  | %examle% |
| 4 | `ATTR_ID2` | DOUBLE |  |  | %examle% |
| 5 | `ATTR_ID3` | DOUBLE |  |  | %examle% |
| 6 | `ATTR_ID4` | DOUBLE |  |  | %examle% |
| 7 | `ATTR_ID5` | DOUBLE |  |  | %examle% |
| 8 | `ATTR_NAME1` | VARCHAR(40) |  |  | %examle% |
| 9 | `ATTR_NAME2` | VARCHAR(40) |  |  | %examle% |
| 10 | `ATTR_NAME3` | VARCHAR(40) |  |  | %examle% |
| 11 | `ATTR_NAME4` | VARCHAR(40) |  |  | %examle% |
| 12 | `ATTR_NAME5` | VARCHAR(40) |  |  | %examle% |
| 13 | `ATTR_VALUE1` | VARCHAR(100) |  |  | %examle% |
| 14 | `ATTR_VALUE2` | VARCHAR(100) |  |  | %examle% |
| 15 | `ATTR_VALUE3` | VARCHAR(100) |  |  | %examle% |
| 16 | `ATTR_VALUE4` | VARCHAR(100) |  |  | %examle% |
| 17 | `ATTR_VALUE5` | VARCHAR(100) |  |  | %examle% |
| 18 | `FIELD_COUNT` | DOUBLE |  |  | The number of fields filled out for this row. |
| 19 | `FIELD_NAME1` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 20 | `FIELD_NAME10` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 21 | `FIELD_NAME2` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 22 | `FIELD_NAME3` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 23 | `FIELD_NAME4` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 24 | `FIELD_NAME5` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 25 | `FIELD_NAME6` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 26 | `FIELD_NAME7` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 27 | `FIELD_NAME8` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 28 | `FIELD_NAME9` | VARCHAR(30) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 29 | `FIELD_VALUE_NEW1` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 30 | `FIELD_VALUE_NEW10` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 31 | `FIELD_VALUE_NEW2` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 32 | `FIELD_VALUE_NEW3` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 33 | `FIELD_VALUE_NEW4` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 34 | `FIELD_VALUE_NEW5` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 35 | `FIELD_VALUE_NEW6` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 36 | `FIELD_VALUE_NEW7` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 37 | `FIELD_VALUE_NEW8` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 38 | `FIELD_VALUE_NEW9` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 39 | `FIELD_VALUE_OLD1` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 40 | `FIELD_VALUE_OLD10` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 41 | `FIELD_VALUE_OLD2` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 42 | `FIELD_VALUE_OLD3` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 43 | `FIELD_VALUE_OLD4` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 44 | `FIELD_VALUE_OLD5` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 45 | `FIELD_VALUE_OLD6` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 46 | `FIELD_VALUE_OLD7` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 47 | `FIELD_VALUE_OLD8` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 48 | `FIELD_VALUE_OLD9` | VARCHAR(100) |  |  | All 'FIELD_*' fields come in threes: Name, Old Value, New Value. The Name will be the actual table field name. The Old Value will contain what was previously on the table and the New Value obviously contains the new one. |
| 49 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 50 | `LOG_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 51 | `LOG_TYPE_CD` | DOUBLE | NOT NULL |  | The type of log. |
| 52 | `ORGANIZATION_ID` | DOUBLE |  | FK→ | The Organization that is associated to the logged item. |
| 53 | `PERSON_NAME` | VARCHAR(100) |  |  | The person who caused the insert. |
| 54 | `REQ_NAME` | VARCHAR(40) |  |  | (currently not used) |
| 55 | `TASK_NAME` | VARCHAR(60) |  |  | The task which caused the insert. |
| 56 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 57 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 58 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 59 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 60 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

